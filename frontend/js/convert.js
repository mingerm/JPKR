const API_BASE = "http://127.0.0.1:5001"; 

    async function convert() {
      const jp = document.getElementById('jp').value.trim();
      const to = document.getElementById('to').value;

      if (!jp) {
        alert("일본어 문장을 입력하세요.");
        return;
      }

      try {
        const res = await fetch(`${API_BASE}/api/convert`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: jp, to }),
          credentials: "include"  
        });

        const data = await res.json();
        if (!res.ok) throw new Error(data.error || "변환 실패");
        document.getElementById('kr').value = data.converted || data.message || "[변환 완료]";
      } catch (err) {
        alert("에러: " + err.message);
      }
    }

    document.getElementById("logoutBtn").addEventListener("click", async () => {
      if (!confirm("로그아웃 하시겠습니까?")) return;
      try {
        await fetch(`${API_BASE}/api/logout`, {
          method: "POST",
          credentials: "include" 
        });
      } catch {}
      alert("로그아웃 되었습니다.");
      window.location.href = "./index.html";
    });