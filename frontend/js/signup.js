// frontend/js/signup.js
const API_BASE = "http://127.0.0.1:5000";

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const idInput = document.getElementById("sid");
    const pwInput = document.getElementById("spswd");

    if (!form) {
      console.error("signup.js: form not found");
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
        const res = await fetch(`${API_BASE}/api/signup`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ id, pswd }),
          credentials: "include"
        });
  
        const data = await res.json();
  
        if (!res.ok) {
          const msg = data.error || data.message || "회원가입 실패";
          throw new Error(msg);
        }
  
        alert("회원가입 완료! 로그인 페이지로 이동합니다.");
        window.location.href = "./index.html";
  
      } catch (err) {
        alert(`회원가입 실패: ${err.message}`);
      }
    });
  });
  