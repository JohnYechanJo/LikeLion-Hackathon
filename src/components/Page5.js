import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import "./Page5.css";

const Page5 = ({ className, ...props }) => {
  const [selectedOption, setSelectedOption] = useState("");
  const navigate = useNavigate();

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleBackClick = () => {
    navigate('/page4'); // Page4로 이동
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // 서버로 데이터를 전송하는 로직을 여기에 추가
    // 예: fetch('/api/submit', { method: 'POST', body: JSON.stringify({ activityLevel: selectedOption }) })
    
    // 데이터를 성공적으로 전송한 후 특정 페이지로 이동
    navigate('/next-page'); // '/next-page'는 특정 페이지의 경로로 변경해야 함
  };

  return (
    <div className={`page5-container ${className}`} {...props}>
      <div className="p5-header">
        <div className="p5-back-arrow" onClick={handleBackClick}>&larr;</div>
        <div className="p5-progress-text">4/4</div>
      </div>
      <form className="p5-form-group" onSubmit={handleSubmit}>
        <div className="p5-form-item">
          <label className="p5-form-label">주로 운동을 얼마나 하시나요?</label>
          <div className="p5-dropdown">
            <select className="p5-dropdown-select" value={selectedOption} onChange={handleOptionChange}>
              <option value="very-low">매우 적음  (사무직)</option>
              <option value="low">약간 활동적 (주 1~3회 운동)</option>
              <option value="moderate">보통 활동적 (주 3~5회 운동)</option>
              <option value="high">매우 활동적 (주 6~7회 운동)</option>
              <option value="very-high">극히 활동적 (하루 2회 운동)</option>
            </select>
          </div>
        </div>
        <div className="p5-confirm-button-container">
          <button type="submit" className="p5-confirm-button">확인</button>
        </div>
      </form>
    </div>
  );
};

export default Page5;