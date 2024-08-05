import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import "./Page1.css";

export const Page1 = ({ className, ...props }) => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSignUpClick = () => {
    navigate('/page2'); 
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/api/login/', formData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      console.log(response.data);
      if (response.data.message === 'Login successful') {
        navigate('/state1'); 
      }
    } catch (error) {
      console.error(error);
      alert('로그인에 실패했습니다. 아이디와 비밀번호를 확인해주세요.');
    }
  };

  return (
    <div className="page1">
      <form onSubmit={handleSubmit}>
        <div className="p1-id-pw-container">
          <div className="p1-id">
            <label htmlFor="username">id</label>
            <input 
              type="text" 
              id="username" 
              name="username" 
              className="p1-input-field" 
              placeholder="아이디" 
              value={formData.username} 
              onChange={handleChange}
              required 
            />
          </div>
          <div className="p1-pw">
            <label htmlFor="password">pw</label>
            <input 
              type="password" 
              id="password" 
              name="password" 
              className="p1-input-field" 
              placeholder="비밀번호" 
              value={formData.password} 
              onChange={handleChange}
              required 
            />
          </div>
        </div>
        <div className="p1-rectangle-28">
          <div className="p1-frame-32">
            <button type="submit" className="p1-rectangle-282">로그인</button>
            <button type="button" className="p1-rectangle-29" onClick={handleSignUpClick}>회원가입</button>
          </div>
        </div>
      </form>
    </div>
  );
};

export default Page1;
