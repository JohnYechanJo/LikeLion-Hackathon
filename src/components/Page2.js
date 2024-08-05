import React from 'react';
import { useNavigate } from 'react-router-dom';
import "./Page2.css";

const Page2 = ({ className, ...props }) => {
  const navigate = useNavigate();

  const handleBackClick = () => {
    navigate('/page1');
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 여기서 서버로 데이터를 전송하는 로직을 추가하세요
    // 예: fetch('/api/submit', { method: 'POST', body: formData })

    // 데이터를 성공적으로 전송한 후 다음 페이지로 이동
    navigate('/page3');
  };

  return (
    <div className={`page2-container ${className}`} {...props}>
      <div className="p2-header">
        <div className="p2-back-arrow" onClick={handleBackClick}>&larr;</div>
        <div className="p2-progress-text">1/4</div>
      </div>
      <form className="p2-form-group" onSubmit={handleSubmit}>
        <div className="p2-form-item">
          <label htmlFor="id-input" className="p2-form-label">id</label>
          <input type="text" id="id-input" className="p2-form-input" />
          <div className="p2-form-divider"></div>
        </div>
        <div className="p2-form-item">
          <label htmlFor="pw-input" className="p2-form-label">pw</label>
          <input type="text" id="pw-input" className="p2-form-input" />
          <div className="p2-form-divider"></div>
        </div>
        <div className="p2-confirm-button-container">
          <button type="submit" className="p2-confirm-button">확인</button>
        </div>
      </form>
    </div>
  );
};

export default Page2;
