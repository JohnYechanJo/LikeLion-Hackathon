import React from 'react';
import { useNavigate } from 'react-router-dom';
import "./Page4.css";

const Page4 = ({ className, ...props }) => {
  const navigate = useNavigate();

  const handleBackClick = () => {
    navigate('/page3');
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 서버로 데이터를 전송하는 로직을 여기에 추가하세요.
    // 예: fetch('/api/submit', { method: 'POST', body: JSON.stringify(formData) })

    // 데이터를 성공적으로 전송한 후 다음 페이지로 이동
    navigate('/page5');
  };

  return (
    <div className={`page4-container ${className}`} {...props}>
      <div className="p4-header">
        <div className="p4-back-arrow" onClick={handleBackClick}>&larr;</div>
        <div className="p4-progress-text">3/4</div>
      </div>
      <form className="p4-form-group" onSubmit={handleSubmit}>
        <div className="p4-form-item">
          <label className="p4-form-label">성별</label>
          <div className="p4-gender-selection">
            <div className="p4-gender-option">
              <input type="checkbox" id="male" name="gender" value="male" />
              <label htmlFor="male" className="p4-gender-label">남자</label>
            </div>
            <div className="p4-gender-option">
              <input type="checkbox" id="female" name="gender" value="female" />
              <label htmlFor="female" className="p4-gender-label">여자</label>
            </div>
          </div>
          <div className="p4-form-divider"></div>
        </div>
        <div className="p4-form-item">
          <label className="p4-form-label">키</label>
          <div className="p4-age-input-group">
            <input type="text" className="p4-form-input small-input" />
            <span className="p4-age-label">cm</span>
          </div>
        </div>
        <div className="p4-form-item">
          <label className="p4-form-label">몸무게</label>
          <div className="p4-age-input-group">
            <input type="text" className="p4-form-input small-input" />
            <span className="p4-age-label">kg</span>
          </div>
        </div>
        <div className="p4-confirm-button-container">
          <button type="submit" className="p4-confirm-button">확인</button>
        </div>
      </form>
    </div>
  );
};

export default Page4;