// Mobile Dropdown Functionality
document.addEventListener("DOMContentLoaded", function () {
  console.log("Script loaded successfully!");

  // Hamburger menu functionality
  const hamburger = document.querySelector(".hamburger-menu");
  const mobileNav = document.querySelector(".mobile-nav");

  console.log("Hamburger element:", hamburger);
  console.log("Mobile nav element:", mobileNav);

  if (hamburger && mobileNav) {
    console.log("Adding click event to hamburger");
    hamburger.addEventListener("click", function () {
      console.log("Hamburger clicked!");
      hamburger.classList.toggle("active");
      mobileNav.classList.toggle("active");
      console.log("Mobile nav active:", mobileNav.classList.contains("active"));
    });
  } else {
    console.log("Hamburger or mobile nav not found!");
  }

  // Mobile dropdown functionality is now handled by inline script to avoid conflicts
});
