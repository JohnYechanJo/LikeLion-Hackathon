import React from 'react';
import { useNavigate } from 'react-router-dom';
import "./Page3.css";

const Page3 = ({ className, ...props }) => {
  const navigate = useNavigate();

  const handleBackClick = () => {
    navigate('/page2');
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 서버로 데이터를 전송하는 로직을 여기에 추가하세요.
    // 예: fetch('/api/submit', { method: 'POST', body: JSON.stringify(formData) })
    
    // 데이터를 성공적으로 전송한 후 다음 페이지로 이동
    navigate('/page4');
  };

  return (
    <div className={`page3-container ${className}`} {...props}>
      <div className="p3-header">
        <div className="p3-back-arrow" onClick={handleBackClick}>&larr;</div>
        <div className="p3-progress-text">2/4</div>
      </div>
      <form className="p3-form-group" onSubmit={handleSubmit}>
        <div className="p3-form-item">
          <label className="p3-form-label">이름을 입력해 주세요</label>
          <input type="text" className="p3-form-input" />
          <div className="p3-form-divider"></div>
        </div>
        <div className="p3-form-item">
          <label className="p3-form-label">나이를 입력해 주세요</label>
          <div className="p3-age-input-group">
            <span className="p3-age-label">만</span>
            <input type="text" className="p3-form-input p3-age-input" />
            <span className="p3-age-label">세</span>
          </div>
          <div className="p3-form-divider"></div>
        </div>
        <div className="p3-form-item">
          <label className="p3-form-label">전화번호를 입력해 주세요</label>
          <div className="p3-phone-inputs">
            <input type="text" className="p3-form-input p3-phone-input"  />
            <span className="p3-phone-label">-</span>
            <input type="text" className="p3-form-input p3-phone-input"  />
            <span className="p3-phone-label">-</span>
            <input type="text" className="p3-form-input p3-phone-input"  />
          </div>
          <div className="p3-form-divider"></div>
        </div>
        <div className="p3-form-item">
          <label className="p3-form-label">이메일을 입력해 주세요</label>
          <div className="p3-email-inputs">
            <input type="text" className="p3-form-input p3-email-input"  />
            <span className="p3-email-label">@</span>
            <input type="text" className="p3-form-input p3-email-input"  />
          </div>
          <div className="p3-form-divider p3-email-divider"></div>
        </div>
        <div className="p3-confirm-button-container">
          <button type="submit" className="p3-confirm-button">확인</button>
        </div>
      </form>
    </div>
  );
};

export default Page3;
