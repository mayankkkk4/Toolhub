/**
 * Calculator & Converter Tools Implementation Module
 */

window.CalcTools = {
  // 1. Scientific Calculator Evaluator
  evaluateExpression: function(expr) {
    if (!expr) return '0';
    try {
      let sanitized = expr
        .replace(/×/g, '*')
        .replace(/÷/g, '/')
        .replace(/π/g, 'Math.PI')
        .replace(/\be\b/g, 'Math.E')
        .replace(/sin\(/g, 'Math.sin(')
        .replace(/cos\(/g, 'Math.cos(')
        .replace(/tan\(/g, 'Math.tan(')
        .replace(/log\(/g, 'Math.log10(')
        .replace(/ln\(/g, 'Math.log(')
        .replace(/sqrt\(/g, 'Math.sqrt(')
        .replace(/\^/g, '**');

      // Use Function constructor for safe math evaluation
      const result = new Function(`return (${sanitized});`)();
      if (typeof result === 'number' && !isNaN(result)) {
        return Number.isInteger(result) ? result.toString() : parseFloat(result.toFixed(8)).toString();
      }
      return 'Error';
    } catch (err) {
      return 'Error';
    }
  },

  // 2. Multi-Unit Converter
  CONVERSION_RATES: {
    length: {
      meter: 1,
      kilometer: 0.001,
      centimeter: 100,
      millimeter: 1000,
      mile: 0.000621371,
      yard: 1.09361,
      foot: 3.28084,
      inch: 39.3701
    },
    weight: {
      kilogram: 1,
      gram: 1000,
      milligram: 1000000,
      pound: 2.20462,
      ounce: 35.274,
      ton: 0.001
    },
    area: {
      sq_meter: 1,
      sq_kilometer: 0.000001,
      sq_mile: 3.861e-7,
      sq_foot: 10.7639,
      acre: 0.000247105,
      hectare: 0.0001
    },
    speed: {
      mps: 1,
      kph: 3.6,
      mph: 2.23694,
      knot: 1.94384
    },
    data: {
      byte: 1,
      kilobyte: 0.001,
      megabyte: 0.000001,
      gigabyte: 1e-9,
      terabyte: 1e-12,
      bit: 8
    },
    time: {
      second: 1,
      minute: 1/60,
      hour: 1/3600,
      day: 1/86400,
      week: 1/604800,
      year: 1/31536000
    }
  },

  convertUnit: function(category, value, fromUnit, toUnit) {
    val = parseFloat(value);
    if (isNaN(val)) return 0;

    if (category === 'temperature') {
      if (fromUnit === toUnit) return val;
      let celsius = val;
      if (fromUnit === 'fahrenheit') celsius = (val - 32) * 5/9;
      if (fromUnit === 'kelvin') celsius = val - 273.15;

      if (toUnit === 'celsius') return parseFloat(celsius.toFixed(4));
      if (toUnit === 'fahrenheit') return parseFloat((celsius * 9/5 + 32).toFixed(4));
      if (toUnit === 'kelvin') return parseFloat((celsius + 273.15).toFixed(4));
    }

    const rates = this.CONVERSION_RATES[category];
    if (rates && rates[fromUnit] && rates[toUnit]) {
      const baseValue = val / rates[fromUnit];
      const result = baseValue * rates[toUnit];
      return parseFloat(result.toFixed(6));
    }
    return 0;
  },

  // 3. Percentage Calculator
  calcPercentage: function(part, total) {
    p = parseFloat(part);
    t = parseFloat(total);
    if (isNaN(p) || isNaN(t) || t === 0) return 0;
    return parseFloat(((p / t) * 100).toFixed(2));
  },

  calcPercentChange: function(initial, finalVal) {
    i = parseFloat(initial);
    f = parseFloat(finalVal);
    if (isNaN(i) || isNaN(f) || i === 0) return 0;
    const diff = f - i;
    return parseFloat(((diff / i) * 100).toFixed(2));
  },

  // 4. Age Calculator
  calcAge: function(birthdateStr) {
    if (!birthdateStr) return null;
    const birthDate = new Date(birthdateStr);
    const today = new Date();
    if (isNaN(birthDate.getTime()) || birthDate > today) return null;

    let years = today.getFullYear() - birthDate.getFullYear();
    let months = today.getMonth() - birthDate.getMonth();
    let days = today.getDate() - birthDate.getDate();

    if (days < 0) {
      months--;
      const lastMonth = new Date(today.getFullYear(), today.getMonth(), 0);
      days += lastMonth.getDate();
    }
    if (months < 0) {
      years--;
      months += 12;
    }

    const diffMs = today.getTime() - birthDate.getTime();
    const totalDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    const totalHours = Math.floor(diffMs / (1000 * 60 * 60));

    return {
      years,
      months,
      days,
      totalDays,
      totalHours
    };
  },

  // 5. Date Difference
  calcDateDiff: function(dateStr1, dateStr2) {
    const d1 = new Date(dateStr1);
    const d2 = new Date(dateStr2);
    if (isNaN(d1.getTime()) || isNaN(d2.getTime())) return null;

    const diffMs = Math.abs(d2.getTime() - d1.getTime());
    const totalDays = Math.floor(diffMs / (1000 * 60 * 60 * 24));
    const weeks = Math.floor(totalDays / 7);
    const remainingDays = totalDays % 7;

    return { totalDays, weeks, remainingDays };
  },

  // 6. BMI Calculator
  calcBMI: function(weight, height, unitSystem = 'metric') {
    w = parseFloat(weight);
    h = parseFloat(height);
    if (isNaN(w) || isNaN(h) || w <= 0 || h <= 0) return null;

    let bmi = 0;
    if (unitSystem === 'metric') {
      // height in cm
      const hMeter = h / 100;
      bmi = w / (hMeter * hMeter);
    } else {
      // weight in lbs, height in inches
      bmi = (w / (h * h)) * 703;
    }

    bmi = parseFloat(bmi.toFixed(1));
    let category = 'Normal weight';
    let badgeClass = 'bg-success';

    if (bmi < 18.5) {
      category = 'Underweight';
      badgeClass = 'bg-warning text-dark';
    } else if (bmi >= 25 && bmi < 29.9) {
      category = 'Overweight';
      badgeClass = 'bg-warning text-dark';
    } else if (bmi >= 30) {
      category = 'Obesity';
      badgeClass = 'bg-danger';
    }

    return { bmi, category, badgeClass };
  }
};
