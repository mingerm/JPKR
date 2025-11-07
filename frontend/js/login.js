// frontend/js/login.js
const API_BASE = "http://127.0.0.1:5000";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const idInput = document.getElementById("id");
    const pwInput = document.getElementById("password");
  
    if (!form) {
      console.error("login.js: form not found");
      return;
    }
  
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
  
      const id = idInput.value.trim();
      const pswd = pwInput.value.trim();
  
      if (!id || !pswd) {
        alert("아이디와 비밀번호를 입력하세요.");
        return;
      }
  
      try {
        const res = await fetch(`${API_BASE}/api/login`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ id, pswd }),
          credentials: "include"
        });
  
        const data = await res.json();
  
        if (!res.ok) {
          const msg = data.error || data.message || "로그인 실패";
          throw new Error(msg);
        }
  
        alert("로그인 성공!");
        // 로그인 성공 시 원하는 페이지로 이동
        window.location.href = "./convert.html";
  
      } catch (err) {
        alert(`로그인 실패: ${err.message}`);
      }
    });
  });
  