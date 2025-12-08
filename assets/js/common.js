// Common JavaScript functions for AlphaAI website
// Transition state management
let isTransitioning = false;
let currentTheme = 'dark';

// Reading progress bar
function updateReadingProgress() {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const progress = (scrollTop / scrollHeight) * 100;
  const progressBar = document.getElementById('readingProgress');
  if (progressBar) {
    progressBar.style.width = progress + '%';
  }
}

// Theme toggle with sunrise/sunset animation
function toggleTheme(event) {
  if (isTransitioning) return;

  const button = event?.target || document.querySelector('.theme-toggle');
  const overlay = document.getElementById('themeOverlay');
  const isLight = document.body.classList.contains('light-theme');
  
  isTransitioning = true;
  
  if (isLight) {
    // Light to Dark - Sunset effect
    overlay.className = 'theme-transition-overlay sunset-gradient sunset-active';
    button.textContent = '🌙';
    
    setTimeout(() => {
      document.body.classList.remove('light-theme');
      localStorage.setItem('theme', 'dark');
      currentTheme = 'dark';
    }, 1500); // Mid-transition
  } else {
    // Dark to Light - Sunrise effect
    overlay.className = 'theme-transition-overlay sunrise-gradient sunrise-active';
    button.textContent = '☀️';
    
    setTimeout(() => {
      document.body.classList.add('light-theme');
      localStorage.setItem('theme', 'light');
      currentTheme = 'light';
    }, 1500); // Mid-transition
  }
  
  // Clean up after animation
  setTimeout(() => {
    overlay.className = 'theme-transition-overlay';
    isTransitioning = false;
  }, 3000);
}

// Helper to clear animation and stagger classes from text elements
function clearTextAnimationClasses(elements) {
  elements.forEach(el => {
    el.classList.remove(
      'text-pop-up',
      'text-pop-down',
      'stagger-text-1',
      'stagger-text-2',
      'stagger-text-3',
      'stagger-text-4',
      'stagger-text-5',
      'stagger-text-6',
      'stagger-text-7',
      'stagger-text-8'
    );
  });
}

// Font size toggle with pop animation
function toggleFontSize(event) {
  if (isTransitioning) return;

  const isLarge = document.body.classList.contains('large-text');
  const textElements = document.querySelectorAll('h1, h2, h3, p, li, a, span');
  const button = event?.target || document.querySelector('.font-control[aria-label="Change text size"]');
  
  if (!isLarge) {
    // Normal to Large - Pop up animation
    textElements.forEach((el, index) => {
      el.classList.add('text-pop-up', `stagger-text-${(index % 8) + 1}`);
    });
    
    document.body.classList.add('large-text');
    localStorage.setItem('largeText', 'true');

    setTimeout(() => {
      clearTextAnimationClasses(textElements);
    }, 1200);
  } else {
    // Large to Normal - Pop down animation
    textElements.forEach((el, index) => {
      el.classList.add('text-pop-down', `stagger-text-${(index % 8) + 1}`);
    });
    
    document.body.classList.remove('large-text');
    localStorage.setItem('largeText', 'false');

    setTimeout(() => {
      clearTextAnimationClasses(textElements);
    }, 800);
  }

  // Update button state
  button?.classList.toggle('active', !isLarge);
}

// High contrast toggle with glitch effect
function toggleContrast(event) {
  if (isTransitioning) return;

  const isHighContrast = document.body.classList.contains('high-contrast');
  const button = event?.target || document.querySelector('.font-control[aria-label="Toggle high contrast"]');
  
  if (!isHighContrast) {
    // Normal to High Contrast - Glitch effect
    document.body.classList.add('glitch-active');
    
    // Create binary rain effect
    for (let i = 0; i < 15; i++) {
      setTimeout(() => {
        const particle = document.createElement('div');
        particle.className = 'binary-particle';
        particle.textContent = Math.random() > 0.5 ? '1' : '0';
        particle.style.left = Math.random() * 100 + '%';
        document.body.appendChild(particle);
        
        setTimeout(() => particle.remove(), 1200);
      }, i * 50);
    }
    
    // Add scan line
    setTimeout(() => {
      const scanLine = document.createElement('div');
      scanLine.className = 'scan-line';
      document.body.appendChild(scanLine);
      
      setTimeout(() => scanLine.remove(), 1500);
    }, 500);
    
    setTimeout(() => {
      document.body.classList.remove('glitch-active');
      document.body.classList.add('high-contrast');
      localStorage.setItem('highContrast', 'true');
    }, 1200);
  } else {
    // High Contrast to Normal - Smooth transition
    document.body.classList.remove('high-contrast');
    localStorage.setItem('highContrast', 'false');
  }

  // Update button state
  button?.classList.toggle('active', !isHighContrast);
}

// Smooth scroll for anchor links
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
}

// Load saved preferences
function loadSavedPreferences() {
  // Theme
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'light') {
    document.body.classList.add('light-theme');
    currentTheme = 'light';
    const themeToggle = document.querySelector('.theme-toggle');
    if (themeToggle) {
      themeToggle.textContent = '☀️';
    }
  }
  
  // Font size
  if (localStorage.getItem('largeText') === 'true') {
    document.body.classList.add('large-text');
  }
  
  // High contrast
  if (localStorage.getItem('highContrast') === 'true') {
    document.body.classList.add('high-contrast');
  }
  
  // Update button states
  const fontButtons = document.querySelectorAll('.font-control');
  fontButtons.forEach(button => {
    if (button.textContent.includes('A+') && localStorage.getItem('largeText') === 'true') {
      button.classList.add('active');
    }
    if (button.textContent.includes('◐') && localStorage.getItem('highContrast') === 'true') {
      button.classList.add('active');
    }
  });
}

// Initialize common functionality
function initCommon() {
  loadSavedPreferences();
  initSmoothScroll();
  
  // Update reading progress on scroll
  window.addEventListener('scroll', updateReadingProgress);
  window.addEventListener('resize', updateReadingProgress);
  
  // Initial progress update
  updateReadingProgress();
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initCommon);
