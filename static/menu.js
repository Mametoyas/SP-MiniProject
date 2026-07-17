/* ═══════════════════════════════════════════
   menu.js — Boot screen → Menu transition
   ═══════════════════════════════════════════ */

// Wait for loading bar animation (1.4s) then show menu
window.addEventListener("DOMContentLoaded", () => {
  setTimeout(() => {
    document.getElementById("boot-screen").style.display  = "none";
    document.getElementById("menu-screen").classList.remove("hidden");
  }, 1600);
});
