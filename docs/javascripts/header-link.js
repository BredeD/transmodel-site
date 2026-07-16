// Make the site title in the header behave as a home link,
// matching the logo icon's behavior. By default Material for MkDocs
// only makes the logo clickable; this extends the click area to the
// site name too.

(function () {
  function makeTitleClickable() {
    const logo = document.querySelector("a.md-header__button.md-logo");
    if (!logo) return;
    const href = logo.getAttribute("href");
    if (!href) return;

    const title = document.querySelector(".md-header__topic .md-ellipsis");
    if (!title) return;

    // Avoid attaching multiple handlers on Material's instant-navigation reloads
    if (title.dataset.homeLinkAdded === "true") return;
    title.dataset.homeLinkAdded = "true";

    title.style.cursor = "pointer";
    title.setAttribute("role", "link");
    title.setAttribute("tabindex", "0");
    title.setAttribute("aria-label", "Go to home page");

    title.addEventListener("click", function () {
      window.location.href = href;
    });

    // Keyboard accessibility: Enter and Space
    title.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        window.location.href = href;
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
