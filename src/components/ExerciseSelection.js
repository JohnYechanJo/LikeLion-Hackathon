import React, { useState } from 'react';
import { FaHeart, FaRunning, FaBicycle, FaSwimmer, FaBasketballBall, FaFutbol, FaDumbbell, FaWalking, FaBaseballBall, FaSkiing, FaTableTennis, FaVolleyballBall } from 'react-icons/fa';

const exerciseIcons = [
  { icon: FaFutbol, label: 'soccer' },
  { icon: FaBasketballBall, label: 'basketball' },
  { icon: FaBaseballBall, label: 'baseball' },
  { icon: FaSwimmer, label: 'swimming' },
  { icon: FaDumbbell, label: 'weightlifting' },
  { icon: FaWalking, label: 'walking' },
  { icon: FaRunning, label: 'running' },
  { icon: FaBicycle, label: 'cycling' },
  { icon: FaSkiing, label: 'skiing' },
  { icon: FaTableTennis, label: 'table tennis' },
  { icon: FaVolleyballBall, label: 'volleyball' }
];

const ExerciseSelection = ({ onConfirm, consumedCalories }) => {
  const [selectedExercises, setSelectedExercises] = useState([]);

  const toggleExerciseSelection = (label) => {
    setSelectedExercises((prevSelectedExercises) =>
      prevSelectedExercises.includes(label)
        ? prevSelectedExercises.filter((exercise) => exercise !== label)
        : [...prevSelectedExercises, label]
    );
  };

  const handleConfirm = () => {
    const selected = exerciseIcons.filter(({ label }) => selectedExercises.includes(label));
    onConfirm(selected);
  };

  return (
    <div style={containerStyle}>
      <div style={contentStyle}>
        <FaHeart style={mainIconStyle} />
        <p style={questionStyle}>어떤 운동을 하실건가요?</p>
        <div style={exerciseGridStyle}>
          {exerciseIcons.map(({ icon: Icon, label }, index) => (
            <div
              key={index}
              style={{
                ...exerciseIconWrapperStyle,
                backgroundColor: selectedExercises.includes(label) ? '#d0eaff' : 'white',
              }}
              onClick={() => toggleExerciseSelection(label)}
            >
              <Icon style={exerciseIconStyle} />
            </div>
          ))}
        </div>
        <button style={confirmButtonStyle} onClick={handleConfirm}>확인</button>
      </div>
    </div>
  );
};

const containerStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  height: '100vh',
  flexDirection: 'column'
};

const contentStyle = {
  textAlign: 'center',
};

const mainIconStyle = {
  width: '50px',
  marginBottom: '20px',
  fontSize: '40px'
};

const questionStyle = {
  fontSize: '18px',
  fontWeight: 'bold',
  marginBottom: '20px'
};

const exerciseGridStyle = {
  display: 'grid',
  gridTemplateColumns: 'repeat(3, 1fr)',
  gap: '10px',
  marginBottom: '20px'
};

const exerciseIconWrapperStyle = {
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  width: '60px',
  height: '60px',
  borderRadius: '50%',
  border: '1px solid #ccc',
  padding: '5px',
  cursor: 'pointer',
  transition: 'background-color 0.3s',
};

const exerciseIconStyle = {
  fontSize: '24px',
};

const confirmButtonStyle = {
  padding: '10px 20px',
  backgroundColor: '#6c63ff',
  color: 'white',
  border: 'none',
  borderRadius: '5px',
  fontSize: '16px',
  cursor: 'pointer',
  transition: 'background-color 0.3s',
};

export default ExerciseSelection;
