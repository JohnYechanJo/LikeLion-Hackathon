import React, { useEffect, useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import './Map.css';
import SearchBar from './SearchBar';
import CategoryButtons from './CategoryButton';

function MapContainer() {
  const mapContainer = useRef(null);
  const [map, setMap] = useState(null);
  const [markers, setMarkers] = useState([]);
  const [lastCenter, setLastCenter] = useState({ lat: 37.5665, lng: 126.9780 });
  const navigate = useNavigate();

  useEffect(() => {
    const kakaoMapScript = document.createElement('script');
    kakaoMapScript.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${process.env.REACT_APP_KAKAO_MAPS_APPKEY}&libraries=services&autoload=false`;
    kakaoMapScript.async = true;

    kakaoMapScript.onload = () => {
      if (window.kakao && window.kakao.maps) {
        window.kakao.maps.load(() => {
          const initialCenter = new window.kakao.maps.LatLng(37.5665, 126.9780);
          const options = {
            center: initialCenter,
            level: 3,
          };
          const mapInstance = new window.kakao.maps.Map(mapContainer.current, options);
          setMap(mapInstance);

          if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition((position) => {
              const currentPosition = new window.kakao.maps.LatLng(position.coords.latitude, position.coords.longitude);
              mapInstance.setCenter(currentPosition);
              setLastCenter({ lat: position.coords.latitude, lng: position.coords.longitude });
            }, (err) => {
              console.error("Geolocation access denied: " + err.message);
            });
          }
        });
      } else {
        console.error('Kakao Maps SDK is not available');
      }
    };

    document.head.appendChild(kakaoMapScript);

    return () => {
      document.head.removeChild(kakaoMapScript);
    };
  }, []);

  const handleSearch = (keyword) => {
    if (!map) return;

    // 기존 마커 제거
    markers.forEach(marker => {
      if (marker && marker.setMap) {
        marker.setMap(null);
      }
    });
    setMarkers([]);

    if (window.kakao && window.kakao.maps && window.kakao.maps.services) {
      const ps = new window.kakao.maps.services.Places();

      ps.keywordSearch(keyword, (data, status) => {
        if (status === window.kakao.maps.services.Status.OK) {
          updateMarkers(data);
        } else {
          alert('검색 결과가 없습니다.');
        }
      }, {
        location: map.getCenter(),
        radius: 5000
      });
    } else {
      console.error('Kakao Maps Services is not available');
    }
  };

  const updateMarkers = (data) => {
    const bounds = new window.kakao.maps.LatLngBounds();
    const newMarkers = data.map(place => {
      const markerPosition = new window.kakao.maps.LatLng(place.y, place.x);
      const marker = new window.kakao.maps.Marker({
        position: markerPosition,
        map: map,
      });

      const infoWindow = new window.kakao.maps.InfoWindow({
        content: `<div class="info-window">
                    <div class="title">${place.place_name}</div>
                    <div>${place.address_name}</div>
                  </div>`
      });

      window.kakao.maps.event.addListener(marker, 'click', () => {
        infoWindow.open(map, marker);
      });

      bounds.extend(markerPosition);
      return {
        marker,
        name: place.place_name,
        address: place.address_name
      };
    });

    setMarkers(newMarkers);
    map.setBounds(bounds);

    // 지도 중심 업데이트
    const center = map.getCenter();
    setLastCenter({ lat: center.getLat(), lng: center.getLng() });
  };

  const handleRecommendationClick = () => {
    // 마커의 이름과 주소 정보를 저장하여 전달
    const markerData = markers.map(markerObj => ({
      name: markerObj.name,
      address: markerObj.address
    }));

    console.log('Navigating to recommendations with markers:', markerData);
    navigate('/recommendations', { state: { markers: markerData } });
  };

  // 지도 보기 버튼 클릭 시 마커 제거 및 마지막 위치로 복원
  const handleMapViewClick = () => {
    markers.forEach(markerObj => {
      if (markerObj.marker && markerObj.marker.setMap) {
        markerObj.marker.setMap(null);
      }
    });
    setMarkers([]);
    if (map) {
      const moveLatLng = new window.kakao.maps.LatLng(lastCenter.lat, lastCenter.lng);
      map.setCenter(moveLatLng);
    }
    navigate('/'); // 기본 경로로 이동
  };

  return (
    <div className="map-wrapper">
      <div className="map-container" ref={mapContainer}>
        <SearchBar onSearch={handleSearch} />
        <CategoryButtons onCategorySelect={handleSearch} />
        <button onClick={handleRecommendationClick} className="recommendation-button">
          리스트 목록
        </button>
        <button onClick={handleMapViewClick} className="back-to-main-button">
          <FontAwesomeIcon icon={faArrowLeft} size="lg" /> {/* 아이콘만 표시 */}
        </button>
      </div>
    </div>
  );
}

export default MapContainer;
