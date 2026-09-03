// Make the site title in the header behave as a home link,
// matching the logo icon's behavior. By default Material for MkDocs
// only makes the logo clickable; this extends the click area to the
// site name too.
//
// The click handler delegates to the real logo <a> element at click
// time, so Material's instant-navigation (SPA) is used and we don't
// capture a stale relative href from the initial page load.

(function () {
  function makeTitleClickable() {
    const title = document.querySelector(".md-header__topic .md-ellipsis");
    if (!title) return;

    // Avoid attaching multiple handlers to the same element
    if (title.dataset.homeLinkAdded === "true") return;
    title.dataset.homeLinkAdded = "true";

    title.style.cursor = "pointer";
    title.setAttribute("role", "link");
    title.setAttribute("tabindex", "0");
    title.setAttribute("aria-label", "Go to home page");

    function go() {
      // Fresh lookup at click time — SPA navigation may have swapped attributes
      const logo = document.querySelector("a.md-header__button.md-logo");
      if (logo && typeof logo.click === "function") {
        logo.click();
      }
    }

    title.addEventListener("click", go);
    title.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        go();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", makeTitleClickable);
  } else {
    makeTitleClickable();
  }

  // Re-run on Material's instant-navigation events
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(makeTitleClickable);
  }
})();
