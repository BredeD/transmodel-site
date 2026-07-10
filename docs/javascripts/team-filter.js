// Team page filter — show/hide members based on the standard they work on.
//
// Each team member card has a data-standards attribute with a comma-separated
// list of standard slugs (transmodel, netex, siri, ojp, opra).
// Members with no known standards (empty attribute) are only shown under "All".
// Filter buttons at the top of the page toggle visibility.

(function () {
  function initTeamFilter() {
    const filterContainer = document.querySelector(".team-filter");
    if (!filterContainer) return;

    const buttons = filterContainer.querySelectorAll("button[data-filter]");
    const members = document.querySelectorAll(".team-member");
    if (!buttons.length || !members.length) return;

    function applyFilter(filter) {
      members.forEach((el) => {
        const raw = (el.dataset.standards || "").trim();
        const standards = raw
          ? raw.split(",").map((s) => s.trim().toLowerCase())
          : [];
        const show = filter === "all" || standards.includes(filter);
        el.style.display = show ? "" : "none";
      });

      buttons.forEach((btn) => {
        btn.classList.toggle("is-active", btn.dataset.filter === filter);
      });

      // Hide any section that has no visible members
      document.querySelectorAll(".team-section").forEach((section) => {
        const visible = section.querySelectorAll(".team-member:not([style*='none'])").length;
        section.style.display = visible ? "" : "none";
      });
    }

    buttons.forEach((btn) => {
      btn.addEventListener("click", () => applyFilter(btn.dataset.filter));
    });

    // Default: show all
    applyFilter("all");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initTeamFilter);
  } else {
    initTeamFilter();
  }

  // Re-init on Material's instant-navigation events
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(initTeamFilter);
  }
})();
