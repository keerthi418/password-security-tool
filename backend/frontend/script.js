// Toggle password visibility
function togglePassword() {
    const passwordInput = document.getElementById('passwordInput');
    const toggleBtn = event.target;
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        toggleBtn.textContent = '🙈';
    } else {
        passwordInput.type = 'password';
        toggleBtn.textContent = '👁️';
    }
}

// Check password strength
async function checkPassword() {
    const password = document.getElementById('passwordInput').value;
    
    if (!password) {
        alert('Please enter a password!');
        return;
    }
    
    try {
        const response = await fetch('http://127.0.0.1:5000/check', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ password: password })
        });
        
        const data = await response.json();
        
        // Show result section
        const resultDiv = document.getElementById('checkResult');
        resultDiv.classList.remove('hidden');
        
        // Update strength bar
        const strengthBar = document.getElementById('strengthBar');
        const strengthLabel = document.getElementById('strengthLabel');
        const scoreLabel = document.getElementById('scoreLabel');
        
        strengthBar.className = 'strength-bar ' + data.strength.toLowerCase();
        strengthLabel.className = 'strength-label ' + data.strength.toLowerCase();
        strengthLabel.textContent = data.strength;
        scoreLabel.textContent = `Score: ${data.score}/7`;
        
        // Update feedback
        const feedbackDiv = document.getElementById('feedbackList');
        feedbackDiv.innerHTML = '';
        data.feedback.forEach(item => {
            const p = document.createElement('p');
            p.textContent = item;
            feedbackDiv.appendChild(p);
        });
        
        // Add common password check
        const commonP = document.createElement('p');
        commonP.textContent = data.common_check;
        commonP.style.fontWeight = 'bold';
        feedbackDiv.appendChild(commonP);
        
    } catch (error) {
        alert('Error checking password: ' + error.message);
    }
}

// Generate password
async function generatePassword() {
    const length = parseInt(document.getElementById('lengthInput').value);
    
    if (length < 8 || length > 32) {
        alert('Password length must be between 8 and 32!');
        return;
    }
    
    try {
        const response = await fetch('http://127.0.0.1:5000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ length: length })
        });
        
        const data = await response.json();
        
        // Show result section
        const resultDiv = document.getElementById('generateResult');
        resultDiv.classList.remove('hidden');
        
        // Display generated password
        document.getElementById('generatedPassword').value = data.password;
        
        // Update strength info
        const genStrengthLabel = document.getElementById('genStrengthLabel');
        const genScoreLabel = document.getElementById('genScoreLabel');
        
        genStrengthLabel.className = 'strength-label ' + data.strength.toLowerCase();
        genStrengthLabel.textContent = data.strength;
        genScoreLabel.textContent = `Score: ${data.score}/7`;
        
    } catch (error) {
        alert('Error generating password: ' + error.message);
    }
}

// Copy password to clipboard
function copyPassword() {
    const passwordField = document.getElementById('generatedPassword');
    passwordField.select();
    document.execCommand('copy');
    
    // Show feedback
    alert('Password copied to clipboard!');
}

// Allow Enter key to check password
document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.getElementById('passwordInput');
    passwordInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            checkPassword();
        }
    });
});

