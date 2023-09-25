document.addEventListener("DOMContentLoaded", function () {
  const toggleSidebarButton = document.getElementById("toggleSidebar");
  const sidebar = document.getElementById("sidebar");

toggleSidebarButton.addEventListener("click", function () {
    if (sidebar.style.width === '250px') {
      sidebar.style.width = '0';
      document.getElementById('content').style.marginLeft = '0';
    } else {
      sidebar.style.width = '250px';
      document.getElementById('content').style.marginLeft = '250px';
    }
  });
});
