import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import logoIcon from './logo.png';
import { FaDumbbell, FaUtensils, FaUser } from 'react-icons/fa';

const containerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  height: '100vh',
  paddingTop: '5%',
  fontFamily: 'Noto Sans KR, sans-serif'
};

const logoStyle = {
  marginBottom: '40px',
  width: '80px',
};

const buttonStyle = {
  marginBottom: '20px',
  padding: '15px 30px',
  backgroundColor: '#e0f7fa',
  border: '1px solid #b2ebf2',
  borderRadius: '12px',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  fontSize: '18px',
  fontWeight: 'bold',
  width: '250px',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
  cursor: 'pointer',
  transition: 'background-color 0.3s, transform 0.3s',
  position: 'relative',
  overflow: 'hidden',
  textDecoration: 'none',
  color: 'black',
};

const iconStyle = {
  marginRight: '10px',
  fontSize: '20px',
};

const textStyle = {
  display: 'inline-block',
  flex: 1,
  textAlign: 'center',
};

const hoverCircleStyle = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  width: '200%',
  height: '200%',
  backgroundColor: 'rgba(0, 0, 0, 0.1)',
  borderRadius: '50%',
  transform: 'translate(-50%, -50%) scale(0)',
  transition: 'transform 0.3s',
  pointerEvents: 'none',
  zIndex: 1,
};

const applyHoverEffect = (buttonRef, hoverCircleRef) => {
  buttonRef.addEventListener('mouseenter', () => {
    hoverCircleRef.style.transform = 'translate(-50%, -50%) scale(1)';
  });

  buttonRef.addEventListener('mouseleave', () => {
    hoverCircleRef.style.transform = 'translate(-50%, -50%) scale(0)';
  });
};

const ButtonWithHoverEffect = ({ onClick, icon: Icon, text }) => {
  const buttonRef = useRef(null);
  const hoverCircleRef = useRef(null);

  useEffect(() => {
    applyHoverEffect(buttonRef.current, hoverCircleRef.current);
  }, []);

  return (
    <button ref={buttonRef} style={buttonStyle} onClick={onClick}>
      <div ref={hoverCircleRef} style={hoverCircleStyle}></div>
      <Icon style={iconStyle} /> <span style={textStyle}>{text}</span>
    </button>
  );
};

const MainScreen = ({ onExerciseRecommendation }) => {
  const navigate = useNavigate();

  return (
    <div style={containerStyle}>
      <img src={logoIcon} alt="Logo Icon" style={logoStyle} />
      <ButtonWithHoverEffect onClick={onExerciseRecommendation} icon={FaDumbbell} text="운동 추천" />
      <ButtonWithHoverEffect icon={FaUtensils} text="음식 추천" onClick={() => navigate('/map')} />
      <ButtonWithHoverEffect icon={FaUser} text="내 정보" onClick={() => navigate('/state1')} />
    </div>
  );
};

export default MainScreen;
