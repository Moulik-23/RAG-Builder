$(document).ready(function () {
  // Animate navbar links
  $(".nav-links a").css({ opacity: 0, right: "-30px", position: "relative" });
  $(".nav-links a").each(function (i) {
    $(this).delay(150 * i).animate({ opacity: 1, right: "0" }, 600);
  });

  // Animate text and buttons
  $(".content h1").css({ opacity: 0, top: "-30px", position: "relative" })
    .animate({ opacity: 1, top: "0" }, 800);

  $(".content .subtitle").css({ opacity: 0, top: "-20px", position: "relative" })
    .delay(300).animate({ opacity: 1, top: "0" }, 800);

  $(".buttons button").css({ opacity: 0, bottom: "-20px", position: "relative" })
    .each(function (i) {
      $(this).delay(400 * i).animate({ opacity: 1, bottom: "0" }, 600);
    });

  // Hover effect
  $(".buttons .btn").hover(
    function () {
      $(this).css({ transform: "scale(1.05)" });
    },
    function () {
      $(this).css({ transform: "scale(1)" });
    }
  );

  // VANTA Background Init
  VANTA.NET({
    el: "body",
    mouseControls: true,
    touchControls: true,
    gyroControls: false,
    minHeight: 200.00,
    minWidth: 200.00,
    scale: 1.0,
    scaleMobile: 1.0,
    color: 0x888888,
    backgroundColor: 0x000000
  });
});
