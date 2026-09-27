/**
 * Security & Privacy Tools Implementation Module
 * 100% Client-Side Privacy: Passwords and files are NEVER uploaded or transmitted.
 */

window.SecTools = {
  // 1. Password & Passphrase Generator
  generatePassword: function(length = 16, useUpper = true, useLower = true, useNums = true, useSyms = true) {
    const uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const lowers = 'abcdefghijklmnopqrstuvwxyz';
    const numbers = '0123456789';
    const symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?';

    let pool = '';
    if (useUpper) pool += uppers;
    if (useLower) pool += lowers;
    if (useNums) pool += numbers;
    if (useSyms) pool += symbols;

    if (!pool) return 'Select at least one character set!';

    const randomValues = new Uint32Array(length);
    window.crypto.getRandomValues(randomValues);

    let result = '';
    for (let i = 0; i < length; i++) {
      result += pool[randomValues[i] % pool.length];
    }
    return result;
  },

  // 2. Password Strength & Entropy Analyzer
  analyzePassword: function(password) {
    if (!password) {
      return { score: 0, entropy: 0, label: 'Empty', color: 'bg-secondary', crackTime: 'Instant', warnings: [] };
    }

    let poolSize = 0;
    if (/[a-z]/.test(password)) poolSize += 26;
    if (/[A-Z]/.test(password)) poolSize += 26;
    if (/[0-9]/.test(password)) poolSize += 10;
    if (/[^a-zA-Z0-9]/.test(password)) poolSize += 32;

    const entropy = Math.round(password.length * Math.log2(poolSize || 1));
    const warnings = [];

    if (password.length < 8) warnings.push('Password is shorter than 8 characters.');
    if (!/[A-Z]/.test(password)) warnings.push('Add uppercase letters.');
    if (!/[0-9]/.test(password)) warnings.push('Add numbers.');
    if (!/[^a-zA-Z0-9]/.test(password)) warnings.push('Add special symbols.');
    if (/^(123456|password|qwerty|admin)/i.test(password)) warnings.push('Contains common predictable word patterns!');

    let score = 0;
    let label = 'Very Weak';
    let color = 'bg-danger';
    let crackTime = 'Instantly';

    if (entropy < 28) {
      score = 20; label = 'Very Weak'; color = 'bg-danger'; crackTime = 'A few seconds';
    } else if (entropy < 40) {
      score = 40; label = 'Weak'; color = 'bg-warning text-dark'; crackTime = 'A few minutes';
    } else if (entropy < 60) {
      score = 60; label = 'Moderate'; color = 'bg-info text-dark'; crackTime = 'A few months';
    } else if (entropy < 80) {
      score = 80; label = 'Strong'; color = 'bg-primary'; crackTime = 'Several decades';
    } else {
      score = 100; label = 'Ultra Secure'; color = 'bg-success'; crackTime = 'Centuries / Billions of years';
    }

    return {
      entropy,
      score,
      label,
      color,
      crackTime,
      length: password.length,
      warnings
    };
  },

  // 3. Web Crypto Hash Generator
  generateHash: async function(text, algo = 'SHA-256') {
    if (!text) return '';
    const msgBuffer = new TextEncoder().encode(text);
    const hashBuffer = await window.crypto.subtle.digest(algo, msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
  },

  // 4. File Checksum Calculator (Web Crypto API)
  calculateFileHash: function(file, algo = 'SHA-256', callback) {
    if (!file) return;
    const reader = new FileReader();
    reader.onload = async function(e) {
      const arrayBuffer = e.target.result;
      const hashBuffer = await window.crypto.subtle.digest(algo, arrayBuffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      const hexHash = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
      callback({
        fileName: file.name,
        fileSize: (file.size / 1024).toFixed(2) + ' KB',
        algorithm: algo,
        hash: hexHash
      });
    };
    reader.readAsArrayBuffer(file);
  },

  // 5. Technical URL Safety & Inspector
  inspectURL: function(inputUrl) {
    let urlObj;
    try {
      urlObj = new URL(inputUrl.startsWith('http') ? inputUrl : 'https://' + inputUrl);
    } catch (e) {
      return { success: false, error: 'Invalid URL format' };
    }

    const warnings = [];
    const technicalData = [];

    technicalData.push({ label: 'Protocol', value: urlObj.protocol });
    technicalData.push({ label: 'Hostname / Domain', value: urlObj.hostname });
    technicalData.push({ label: 'Path', value: urlObj.pathname || '/' });
    technicalData.push({ label: 'Query Parameters', value: urlObj.search || 'None' });

    if (urlObj.protocol === 'http:') {
      warnings.push('Unencrypted Protocol (HTTP): Data sent over this link is unencrypted.');
    }

    if (urlObj.hostname.split('.').length > 4) {
      warnings.push('Excessive Subdomains: Suspicious multi-level subdomain structure detected.');
    }

    if (/@/.test(urlObj.href)) {
      warnings.push('User Credentials in URL: URL contains "@" symbol, often used in phishing redirects.');
    }

    if (/\.(exe|zip|scr|vbs|bat|sh)$/i.test(urlObj.pathname)) {
      warnings.push('Direct Executable File Link: URL directly targets an executable or archive file.');
    }

    return {
      success: true,
      href: urlObj.href,
      domain: urlObj.hostname,
      technicalData: technicalData,
      warnings: warnings,
      disclaimer: "Privacy & Technical Disclaimer: Static heuristic checks identify structural red flags. ToolHub does not replace a live anti-malware threat database."
    };
  }
};
