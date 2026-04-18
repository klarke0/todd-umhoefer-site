// Todd Umhoefer — animations
// Scroll-based reveal via IntersectionObserver.
// Add data-animate to any element to have it fade/slide in on scroll.

(function () {
  'use strict';

  var elements = document.querySelectorAll('[data-animate]');
  if (!elements.length) return;

  if (!('IntersectionObserver' in window)) {
    // Fallback: just show everything immediately
    elements.forEach(function (el) { el.classList.add('is-visible'); });
    return;
  }

  var observer = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.1,
    rootMargin: '0px 0px -48px 0px'
  });

  elements.forEach(function (el) { observer.observe(el); });
}());
