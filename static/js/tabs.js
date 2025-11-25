document.addEventListener('DOMContentLoaded', function() {
  const tabContainers = document.querySelectorAll('[data-tabs]');

  tabContainers.forEach(function(container) {
    const tabs = container.querySelectorAll('.tabs__tab');
    const panels = container.querySelectorAll('.tabs__panel');

    tabs.forEach(function(tab) {
      tab.addEventListener('click', function() {
        const targetIndex = this.getAttribute('data-tab');

        // Update tabs
        tabs.forEach(function(t) {
          t.classList.remove('tabs__tab--active');
          t.setAttribute('aria-selected', 'false');
        });
        this.classList.add('tabs__tab--active');
        this.setAttribute('aria-selected', 'true');

        // Update panels
        panels.forEach(function(panel) {
          const panelIndex = panel.getAttribute('data-panel');
          if (panelIndex === targetIndex) {
            panel.classList.add('tabs__panel--active');
            panel.removeAttribute('hidden');
          } else {
            panel.classList.remove('tabs__panel--active');
            panel.setAttribute('hidden', '');
          }
        });
      });
    });
  });
});
