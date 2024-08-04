import React, { useState } from 'react';
import { FaUtensils, FaHamburger, FaPizzaSlice, FaDrumstickBite, FaFish, FaBreadSlice, FaCarrot, FaIceCream, FaAppleAlt, FaCookie, FaEgg } from 'react-icons/fa';

const foodIcons = [
  { icon: FaHamburger, label: 'burger', calories: 300 },
  { icon: FaPizzaSlice, label: 'pizza', calories: 270 },
  { icon: FaDrumstickBite, label: 'chicken', calories: 250 },
  { icon: FaFish, label: 'fish', calories: 200 },
  { icon: FaBreadSlice, label: 'bread', calories: 80 },
  { icon: FaCarrot, label: 'carrot', calories: 25 },
  { icon: FaIceCream, label: 'ice-cream', calories: 200 },
  { icon: FaAppleAlt, label: 'apple', calories: 95 },
  { icon: FaCookie, label: 'cookie', calories: 160 },
  { icon: FaEgg, label: 'egg', calories: 70 }
];

const ExerciseRecommendation = ({ onNext }) => {
  const [selectedFoods, setSelectedFoods] = useState([]);

  const toggleFoodSelection = (label) => {
    setSelectedFoods((prevSelectedFoods) =>
      prevSelectedFoods.includes(label)
        ? prevSelectedFoods.filter((food) => food !== label)
        : [...prevSelectedFoods, label]
    );
  };

  const handleNext = () => {
    const totalCalories = selectedFoods.reduce((acc, label) => {
      const food = foodIcons.find((item) => item.label === label);
      return acc + (food ? food.calories : 0);
    }, 0);
    onNext(totalCalories);
  };

  return (
    <div style={containerStyle}>
      <div style={contentStyle}>
        <FaUtensils style={mainIconStyle} />
        <p style={questionStyle}>어떤 음식을 드셨나요?</p>
        <div style={foodGridStyle}>
          {foodIcons.map(({ icon: Icon, label }, index) => (
            <div
              key={index}
              style={{
                ...foodIconWrapperStyle,
                backgroundColor: selectedFoods.includes(label) ? '#d0eaff' : 'white',
              }}
              onClick={() => toggleFoodSelection(label)}
            >
              <Icon style={foodIconStyle} />
            </div>
          ))}
        </div>
        <button style={nextButtonStyle} onClick={handleNext}>다음</button>
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

const foodGridStyle = {
  display: 'grid',
  gridTemplateColumns: 'repeat(3, 1fr)',
  gap: '10px',
  marginBottom: '20px'
};

const foodIconWrapperStyle = {
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

const foodIconStyle = {
  fontSize: '24px',
};

const nextButtonStyle = {
  padding: '10px 20px',
  backgroundColor: '#6c63ff',
  color: 'white',
  border: 'none',
  borderRadius: '5px',
  fontSize: '16px',
  cursor: 'pointer',
  transition: 'background-color 0.3s',
};

export default ExerciseRecommendation;
