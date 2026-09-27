/**
 * Developer Tools Implementation Module
 */

window.DevTools = {
  // 1. JSON Formatter, Minifier & Validator
  formatJSON: function(inputStr, indent = 2) {
    if (!inputStr.trim()) return { success: false, error: 'Input cannot be empty' };
    try {
      const parsed = JSON.parse(inputStr);
      const formatted = JSON.stringify(parsed, null, indent);
      return { success: true, result: formatted, parsed: parsed };
    } catch (err) {
      return { success: false, error: err.message };
    }
  },

  minifyJSON: function(inputStr) {
    if (!inputStr.trim()) return { success: false, error: 'Input cannot be empty' };
    try {
      const parsed = JSON.parse(inputStr);
      return { success: true, result: JSON.stringify(parsed) };
    } catch (err) {
      return { success: false, error: err.message };
    }
  },

  validateJSON: function(inputStr) {
    if (!inputStr.trim()) return { valid: false, message: 'Input is empty' };
    try {
      JSON.parse(inputStr);
      return { valid: true, message: 'Valid JSON Syntax' };
    } catch (err) {
      return { valid: false, message: err.message };
    }
  },

  // 2. Base64 Encoder / Decoder
  base64Encode: function(str) {
    try {
      const encoded = btoa(unescape(encodeURIComponent(str)));
      return { success: true, result: encoded };
    } catch (err) {
      return { success: false, error: 'Failed to encode: ' + err.message };
    }
  },

  base64Decode: function(str) {
    try {
      const decoded = decodeURIComponent(escape(atob(str.trim())));
      return { success: true, result: decoded };
    } catch (err) {
      return { success: false, error: 'Invalid Base64 string' };
    }
  },

  // 3. URL Encoder / Decoder
  urlEncode: function(str) {
    return encodeURIComponent(str);
  },

  urlDecode: function(str) {
    try {
      return decodeURIComponent(str);
    } catch (e) {
      return 'Invalid URL encoded text';
    }
  },

  // 4. JWT Decoder
  decodeJWT: function(jwtStr) {
    const parts = jwtStr.trim().split('.');
    if (parts.length !== 3) {
      return { success: false, error: 'Invalid JWT structure (must have 3 dot-separated parts)' };
    }
    try {
      const header = JSON.parse(atob(parts[0].replace(/-/g, '+').replace(/_/g, '/')));
      const payload = JSON.parse(atob(parts[1].replace(/-/g, '+').replace(/_/g, '/')));
      return {
        success: true,
        header: JSON.stringify(header, null, 2),
        payload: JSON.stringify(payload, null, 2),
        signature: parts[2]
      };
    } catch (err) {
      return { success: false, error: 'Failed to decode JWT base64 payload: ' + err.message };
    }
  },

  // 5. UUID / GUID Generator
  generateUUID: function(count = 5, uppercase = false, hyphenated = true) {
    const uuids = [];
    for (let i = 0; i < count; i++) {
      let uuid = crypto.randomUUID();
      if (!hyphenated) uuid = uuid.replace(/-/g, '');
      if (uppercase) uuid = uuid.toUpperCase();
      uuids.push(uuid);
    }
    return uuids.join('\n');
  },

  // 6. Regex Tester
  testRegex: function(pattern, flags, text) {
    if (!pattern) return { success: false, error: 'Pattern is required' };
    try {
      const regex = new RegExp(pattern, flags);
      const matches = [];
      let match;

      if (flags.includes('g')) {
        while ((match = regex.exec(text)) !== null) {
          matches.push({ index: match.index, match: match[0], groups: match.slice(1) });
          if (match.index === regex.lastIndex) regex.lastIndex++; // avoid infinite loop
        }
      } else {
        match = regex.exec(text);
        if (match) {
          matches.push({ index: match.index, match: match[0], groups: match.slice(1) });
        }
      }
      return { success: true, count: matches.length, matches: matches };
    } catch (err) {
      return { success: false, error: err.message };
    }
  },

  // 7. Unix Timestamp Converter
  convertTimestamp: function(inputVal) {
    let date;
    const isNum = /^\d+$/.test(String(inputVal).trim());
    if (isNum) {
      let ts = parseInt(inputVal, 10);
      if (ts < 10000000000) ts *= 1000; // convert seconds to ms
      date = new Date(ts);
    } else {
      date = new Date(inputVal);
    }

    if (isNaN(date.getTime())) {
      return { success: false, error: 'Invalid Date or Timestamp' };
    }

    return {
      success: true,
      unixSeconds: Math.floor(date.getTime() / 1000),
      unixMs: date.getTime(),
      iso: date.toISOString(),
      utc: date.toUTCString(),
      local: date.toLocaleString()
    };
  },

  // 8. Color Code Converter
  convertColor: function(inputStr) {
    inputStr = inputStr.trim();
    let r=0, g=0, b=0;

    if (inputStr.startsWith('#')) {
      let hex = inputStr.replace('#', '');
      if (hex.length === 3) hex = hex.split('').map(c => c+c).join('');
      if (hex.length === 6) {
        r = parseInt(hex.substring(0, 2), 16);
        g = parseInt(hex.substring(2, 4), 16);
        b = parseInt(hex.substring(4, 6), 16);
      }
    } else if (inputStr.toLowerCase().startsWith('rgb')) {
      const matches = inputStr.match(/\d+/g);
      if (matches && matches.length >= 3) {
        r = parseInt(matches[0]);
        g = parseInt(matches[1]);
        b = parseInt(matches[2]);
      }
    } else {
      return { success: false, error: 'Enter a valid HEX (e.g. #6366f1) or RGB (e.g. rgb(99, 102, 241))' };
    }

    r = Math.min(255, Math.max(0, r));
    g = Math.min(255, Math.max(0, g));
    b = Math.min(255, Math.max(0, b));

    const hex = "#" + ((1 << 24) + (r << 16) + (g << 8) + b).toString(16).slice(1);
    
    // HSL Conversion
    let rNorm = r / 255, gNorm = g / 255, bNorm = b / 255;
    let max = Math.max(rNorm, gNorm, bNorm), min = Math.min(rNorm, gNorm, bNorm);
    let h, s, l = (max + min) / 2;

    if (max === min) {
      h = s = 0;
    } else {
      let d = max - min;
      s = l > 0.5 ? d / (2 - max - min) : d / (max + min);
      switch (max) {
        case rNorm: h = (gNorm - bNorm) / d + (gNorm < bNorm ? 6 : 0); break;
        case gNorm: h = (bNorm - rNorm) / d + 2; break;
        case bNorm: h = (rNorm - gNorm) / d + 4; break;
      }
      h /= 6;
    }

    return {
      success: true,
      hex: hex.toUpperCase(),
      rgb: `rgb(${r}, ${g}, ${b})`,
      hsl: `hsl(${Math.round(h * 360)}, ${Math.round(s * 100)}%, ${Math.round(l * 100)}%)`,
      r: r, g: g, b: b
    };
  },

  // 9. Simple Code Formatters (HTML, CSS, JS, SQL)
  formatHTML: function(html) {
    let formatted = '', indent = '';
    const tab = '  ';
    html.split(/>\s*</).forEach(element => {
      if (element.match(/^\/\w/)) {
        indent = indent.substring(tab.length);
      }
      formatted += indent + '<' + element + '>\r\n';
      if (element.match(/^<?\w[^>]*[^\/]$/) && !element.startsWith("input") && !element.startsWith("img") && !element.startsWith("br") && !element.startsWith("hr")) {
        indent += tab;
      }
    });
    return formatted.substring(1, formatted.length - 3);
  },

  formatCSS: function(css) {
    return css
      .replace(/\s*\{\s*/g, " {\n  ")
      .replace(/\s*;\s*/g, ";\n  ")
      .replace(/\s*\}\s*/g, "\n}\n\n")
      .replace(/  \}/g, "}");
  },

  formatSQL: function(sql) {
    const keywords = ["SELECT", "FROM", "WHERE", "AND", "OR", "GROUP BY", "ORDER BY", "HAVING", "LIMIT", "JOIN", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN", "INSERT INTO", "VALUES", "UPDATE", "SET", "DELETE"];
    let formatted = sql;
    keywords.forEach(kw => {
      const reg = new RegExp(`\\b${kw}\\b`, 'gi');
      formatted = formatted.replace(reg, `\n${kw.toUpperCase()}`);
    });
    return formatted.trim();
  }
};
