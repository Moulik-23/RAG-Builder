// upload_script.js

const API_BASE_URL = "http://localhost:8000/api";

$(document).ready(function () {
  const fileInput = $("#docFile");
  const uploadBtn = $("#uploadBtn");
  const projectNameInput = $("#projectName");
  const chatSection = $("#chatInterface");
  const loadingOverlay = $("#loadingOverlay");

  const session_id = localStorage.getItem("session_id") || crypto.randomUUID();
  localStorage.setItem("session_id", session_id);

  // Load project table
  loadProjects();

  uploadBtn.click(async function () {
    const file = fileInput[0]?.files[0];
    const projectName = projectNameInput.val().trim();

    if (!file || !projectName) {
      toastr.error("Please provide both project name and document.");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("session_id", session_id);

    try {
      loadingOverlay.show();

      const response = await fetch(`${API_BASE_URL}/upload-docs`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) throw new Error("Upload failed");

      const result = await response.json();
      console.log("Upload result:", result);

      const project = {
        name: projectName,
        type: "Document",
        date: new Date().toISOString().split("T")[0],
        status: "✅ Ready",
        session_id,
      };

      saveProject(project);
      toastr.success("RAG App Ready! Redirecting to chat...");

      setTimeout(() => {
        window.location.href = `chat.html?session_id=${session_id}&name=${encodeURIComponent(
          projectName
        )}`;
      }, 2000);
    } catch (err) {
      console.error(err);
      toastr.error("Upload failed. Please try again.");
    } finally {
      loadingOverlay.hide();
    }
  });

  function saveProject(project) {
    const projects = JSON.parse(localStorage.getItem("projects") || "[]");
    projects.push(project);
    localStorage.setItem("projects", JSON.stringify(projects));
    loadProjects(); // Refresh UI
  }

  function loadProjects() {
    const projects = JSON.parse(localStorage.getItem("projects") || "[]");
    const tbody = $(".table-section tbody");
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

    // Attach chat button
    $(".chat-btn").click(function () {
      const sessionId = $(this).data("session");
      const name = $(this).data("name");
      localStorage.setItem("active_project_name", name);
      window.location.href = `chat.html?session_id=${sessionId}&name=${encodeURIComponent(
        name
      )}`;
    });

    // Attach delete button
    $(".delete-btn").click(function () {
      const index = $(this).data("index");
      const projects = JSON.parse(localStorage.getItem("projects") || "[]");
      projects.splice(index, 1);
      localStorage.setItem("projects", JSON.stringify(projects));
      loadProjects();
    });
  }
});
