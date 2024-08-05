import React, { useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import logoIcon from './logo.png';
import { FaDumbbell, FaUtensils, FaUser } from 'react-icons/fa';

const appContainerStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  height: '100vh',
  backgroundColor: '#333', // 배경색을 조금 더 밝게 조정
  margin: 0, // 회색 배경 제거
};

const containerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  height: '100%',
  width: '375px', // 핸드폰 크기
  paddingTop: '0',
  fontFamily: 'Noto Sans KR, sans-serif',
  backgroundColor: '#2e2e2e', // 어두운 배경색 적용
  borderRadius: '15px', // 살짝 둥근 모서리
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.3)', // 그림자 추가
  overflow: 'hidden', // 회색 배경 제거
};

const headerStyle = {
  display: 'flex',
  justifyContent: 'space-between',
  alignItems: 'center',
  width: '100%',
  padding: '10px 15px', // 상단 바의 크기 줄이기
  backgroundColor: '#fff', // 상단 배경을 흰색으로 설정
  borderTopLeftRadius: '15px',
  borderTopRightRadius: '15px',
};

const logoStyle = {
  width: '60px', // 로고 크기 조정
  height: '60px',
  borderRadius: '50%', // 동그랗게 자르기
  objectFit: 'cover',
};

const authButtonContainerStyle = {
  display: 'flex',
  alignItems: 'center',
};

const authButtonStyle = {
  color: '#000',
  fontSize: '12px',
  fontWeight: 'bold',
  textDecoration: 'none',
  marginLeft: '5px',
  cursor: 'pointer',
};

const buttonWrapperStyle = {
  marginTop: '30px', // 상단 바와 박스들 사이에 여백 추가
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
};

const buttonContainerStyle = {
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'center',
  marginBottom: '20px',
  position: 'relative',
};

const buttonStyle = {
  width: '80px',
  height: '80px',
  backgroundColor: '#fff',
  border: '2px solid #007bff',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
  fontSize: '16px',
  fontWeight: 'bold',
  cursor: 'pointer',
  transition: 'transform 0.3s, background-color 0.3s, color 0.3s, margin-right 0.3s',
  position: 'relative',
  overflow: 'hidden',
  textDecoration: 'none',
  color: '#007bff',
  borderRadius: '12px',
  boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
};

const iconStyle = {
  fontSize: '40px',
  transition: 'opacity 0.3s',
  color: '#007bff', // Icon color updated to blue
};

const textStyle = {
  fontSize: '18px',
  fontWeight: 'bold',
  color: '#fff',
  marginTop: '10px',
};

const applyHoverEffect = (buttonRef, textRef) => {
  buttonRef.addEventListener('mouseenter', () => {
    buttonRef.style.transform = 'translateY(-10px)';  // 버튼이 위로 이동
    textRef.style.color = '#fff';  // 텍스트 색상 변경
  });

  buttonRef.addEventListener('mouseleave', () => {
    buttonRef.style.transform = 'translateY(0)';  // 버튼이 원래 위치로 돌아옴
    textRef.style.color = '#000';  // 텍스트 색상 원래대로
  });
};

const ButtonWithHoverEffect = ({ onClick, icon: Icon, text }) => {
  const buttonRef = useRef(null);
  const textRef = useRef(null);

  useEffect(() => {
    applyHoverEffect(buttonRef.current, textRef.current);
  }, []);

  return (
    <div style={buttonContainerStyle}>
      <button ref={buttonRef} style={buttonStyle} onClick={onClick}>
        <Icon style={iconStyle} />
      </button>
      <span ref={textRef} style={textStyle}>{text}</span>
    </div>
  );
};

const MainScreen = ({ onExerciseRecommendation }) => {
  const navigate = useNavigate();

  return (
    <div style={appContainerStyle}>
      <div style={containerStyle}>
        <div style={headerStyle}>
          <img src={logoIcon} alt="Logo Icon" style={logoStyle} />
          <div style={authButtonContainerStyle}>
            <span style={authButtonStyle} onClick={() => navigate('/login')}>로그인</span>
            <span style={{ ...authButtonStyle, marginLeft: '5px', marginRight: '5px' }}>/</span>
            <span style={{ ...authButtonStyle, marginRight: '10px' }} onClick={() => navigate('/signup')}>회원가입</span> {/* 우측으로 띄어쓰기 추가 */}
          </div>
        </div>
        <div style={buttonWrapperStyle}>
          <ButtonWithHoverEffect onClick={onExerciseRecommendation} icon={FaDumbbell} text="운동 추천" />
          <ButtonWithHoverEffect icon={FaUtensils} text="음식 추천" onClick={() => navigate('/map')} />
          <ButtonWithHoverEffect icon={FaUser} text="내 정보" onClick={() => navigate('/state1')} />
        </div>
      </div>
    </div>
  );
};

export default MainScreen;
