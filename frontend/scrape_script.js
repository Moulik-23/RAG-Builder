const API_BASE_URL = "http://localhost:8000/api";

$(document).ready(function () {
  const scrapeBtn = $("#uploadBtn");
  const urlInput = $("#urlInput");
  const projectNameInput = $("#projectName");
  const loadingOverlay = $("#loadingOverlay");

  const session_id = localStorage.getItem("session_id") || crypto.randomUUID();
  localStorage.setItem("session_id", session_id);

  loadProjects(); // Load existing projects on page load

  scrapeBtn.click(async function () {
    const url = urlInput.val().trim();
    const projectName = projectNameInput.val().trim();

    if (!projectName || !url) {
      toastr.error("Please enter both project name and website URL.");
      return;
    }

    loadingOverlay.show();

    try {
      const response = await fetch(
        `${API_BASE_URL}/scrape?url=${encodeURIComponent(url)}&max_depth=1`,
        {
          method: "POST",
        }
      );

      if (!response.ok) throw new Error("Scraping failed");

      const result = await response.json();

      const project = {
        name: projectName,
        type: "🌐 Web",
        date: new Date().toISOString().split("T")[0],
        status: "✅ Ready",
        session_id: result.session_id,
      };

      saveProject(project);
      toastr.success("Scraping completed. Project added!");

      window.location.href = `chat.html?session_id=${
        project.session_id
      }&name=${encodeURIComponent(projectName)}`;

      // Reset input fields
      urlInput.val("");
      projectNameInput.val("");
    } catch (err) {
      console.error(err);
      toastr.error("Failed to create RAG from website.");
    } finally {
      loadingOverlay.hide();
    }
  });

  function saveProject(project) {
    const projects = JSON.parse(localStorage.getItem("projects") || "[]");
    projects.push(project);
    localStorage.setItem("projects", JSON.stringify(projects));
    loadProjects();
  }

  function loadProjects() {
    const projects = JSON.parse(localStorage.getItem("projects") || "[]");
    const tbody = $("#projectsTableBody");
    tbody.empty();

    projects.forEach((p, index) => {
      const row = `
        <tr>
          <td>${p.name}</td>
          <td>${p.type}</td>
          <td>${p.date}</td>
          <td>${p.status}</td>
          <td>
            <button class="chat-btn" data-session="${p.session_id}" data-name="${p.name}">💬 Chat</button>
            <button class="delete-btn" data-index="${index}">🗑️</button>
          </td>
        </tr>
      `;
      tbody.append(row);
    });

    $(".chat-btn").click(function () {
      const sessionId = $(this).data("session");
      const name = $(this).data("name");
      localStorage.setItem("active_project_name", name);
      window.location.href = `chat.html?session_id=${sessionId}&name=${encodeURIComponent(
        name
      )}`;
    });

    $(".delete-btn").click(function () {
      const index = $(this).data("index");
      const projects = JSON.parse(localStorage.getItem("projects") || "[]");
      projects.splice(index, 1);
      localStorage.setItem("projects", JSON.stringify(projects));
      loadProjects();
    });
  }
});
