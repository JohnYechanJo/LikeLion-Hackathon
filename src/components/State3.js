import React from 'react';
import "./State3.css";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCalendarDays } from '@fortawesome/free-regular-svg-icons';
import { faDumbbell  } from '@fortawesome/free-solid-svg-icons';
import { faChartSimple } from '@fortawesome/free-solid-svg-icons';
import { useState, useEffect } from 'react';
import axios from 'axios';
import { faArrowLeft } from '@fortawesome/free-solid-svg-icons';
import { faHouse } from '@fortawesome/free-solid-svg-icons';
import { useNavigate } from 'react-router-dom';

const State3 = ({ className, ...props }) => {

    
    const [consumedKcal, setConsumedKcal] = useState(0);
    const [basalMetabolicRate, setBasalMetabolicRate] = useState(0);
    const navigate = useNavigate();
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/data/', {
                    responseType: 'json',
                });
                setConsumedKcal(response.data.consumedKcal);
                setBasalMetabolicRate(response.data.basalMetabolicRate);
            } catch (error) {
                console.error('Error fetching data:', error);
            }
        };

        fetchData();
    }, []);

    const percentBurned = Math.min((consumedKcal / (consumedKcal + basalMetabolicRate)) * 100, 100);
    const currentDate = new Date().toLocaleDateString('ko-KR', { month: '2-digit', day: '2-digit' });

    return (
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'flex-start', alignItems: 'center', height: '100vh', width: '100vw', marginBottom: 0, backgroundColor: '#F3F4F8' }}>
            <div style={{ marginTop:"20px" , width: '350px', height: '62px', display: 'flex', flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginLeft: 0, color: '#F3F4F8', backgroundColor: '#F3F4F8', borderRadius: '10px' }}>
                <FontAwesomeIcon icon={faArrowLeft} style={{ color: '#000000', fontSize: 24 }} onClick={() => navigate('/state1')} />
                <div className="Calender" style={{ width: 166, height: 47, background: '#B1B8C0', borderRadius: 12, justifyContent: 'flex-start', alignItems: 'center', gap: 16, display: 'inline-flex' }}>
                    <div className="IconCalender" style={{ width: 44, height: 30, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                        <FontAwesomeIcon icon={faCalendarDays} style={{ color: '#000000', fontSize: 24 }} />
                    </div>
                    <div className="Date" style={{ width: 106, height: 47, color: '#000000', fontSize: 24, fontFamily: 'Noto Sans KR', justifyContent: 'center', alignItems: 'center', fontWeight: '700', wordWrap: 'break-word', display: 'flex' }}>
                        {currentDate}
                    </div>
                </div>
                <FontAwesomeIcon icon={faHouse} style={{ color: '#000000', fontSize: 24 }} onClick={() => navigate('/')}/>
            </div>

            <div className="border-line0" style={{ width: '80%', borderTop: '3px solid #F3F4F8', borderRadius: '2px', marginTop: '10px', marginBottom: '10px' }}></div>

            <div className="Consumekcal" style={{ color: '#ffffff', backgroundColor: '#ffffff', borderRadius: '10px', width: 390, height: 120, flexDirection: 'column', justifyContent: 'flex-start', alignItems: 'flex-start', gap: 5, display: 'inline-flex' }}>
                <div style={{ marginTop: '10px', marginLeft: '25.5px', alignSelf: 'stretch', color: 'black', fontSize: 18, fontFamily: 'Noto Sans KR', fontWeight: '800', wordWrap: 'break-word' }}>소모한 칼로리    <span style={{ fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '600', wordWrap: 'break-word' }}>(kcal)</span></div>
                <div className="Consumegraph" style={{ marginLeft: '25.5px', width: 338, height: 33, position: 'relative' }}>
                    <div className="Rectangle11" style={{ width: 338, height: 33, left: 0, top: 0, position: 'absolute', background: '#B5D4F1', borderRadius: 10 }}>
                    <div className="Rectangle12" style={{ width: `${percentBurned}%`, height: '100%', background: '#3D81BE', borderRadius: 10 }} />
                    </div> 
                </div>
                <div className="Frame42" style={{ marginLeft: '25.5px', alignSelf: 'stretch', justifyContent: 'flex-start', alignItems: 'center', gap: 121, display: 'inline-flex' }}>
                    <div className="Kcal" style={{ width: 33, height: 29, color: 'black', fontSize: 13, fontFamily: 'Noto Sans KR', fontWeight: '700', wordWrap: 'break-word' }}>0</div>
                    <div className="Kcal" style={{ width: 33, height: 29, color: 'black', fontSize: 13, fontFamily: 'Noto Sans KR', fontWeight: '700', wordWrap: 'break-word' }}>1500</div>
                    <div className="Kcal" style={{ width: 33, height: 29, color: 'black', fontSize: 13, fontFamily: 'Noto Sans KR', fontWeight: '700', wordWrap: 'break-word' }}>3000</div>
                </div>

            </div>


            <div className="border-line1" style={{ width: '80%', borderTop: '3px solid #F3F4F8', borderRadius: '2px', marginTop: '20px', marginBottom: '15px' }}></div>

            <div className="Whattoeat" style={{ color: '#ffffff', backgroundColor: '#ffffff', width: 390, borderRadius: '10px', height: 300, flexDirection: 'column', justifyContent: 'center', alignItems: 'center', gap: 5, display: 'inline-flex' }}>
                <div className="Frame6" style={{ alignSelf: 'stretch', justifyContent: 'flex-start', alignItems: 'center', gap: 13, display: 'inline-flex', marginLeft: 25.5, marginTop: 20 }}>
                    <FontAwesomeIcon icon={faDumbbell} style={{ color: '#000000', fontSize: 24, fontWeight: 200 }} />
                    <div style={{ width: 137, textAlign: 'center', color: '#BDC6FF', fontSize: 24, fontFamily: 'Noto Sans KR', fontWeight: '700', wordWrap: 'break-word' }}>내가 한 운동</div>
                </div>
                <div className="Frame36" style={{ width: 339, flex: '1 1 0', flexDirection: 'column', justifyContent: 'center', alignItems: 'flex-start', gap: 21, display: 'inline-flex' }}>
                    <div className="Frame7" style={{ alignSelf: 'stretch', justifyContent: 'flex-start', alignItems: 'center', gap: 36, display: 'inline-flex' }}>
                        <div className="Rectangle10" style={{ width: 150, height: 90, background: '#D9D9D9', borderRadius: 60 }} />
                        <div className="Rectangle12" style={{ width: 150, height: 90, background: '#D9D9D9', borderRadius: 60 }} />
                    </div>
                    <div className="Frame38" style={{ alignSelf: 'stretch', justifyContent: 'space-between', alignItems: 'center', display: 'inline-flex' }}>
                        <div className="Rectangle14" style={{ width: 150, height: 90, background: '#D9D9D9', borderRadius: 60 }}></div>
                        <div className="Rectangle15" style={{ width: 150, height: 90, background: '#D9D9D9', borderRadius: 60 }}></div>
                    </div>
                </div>
            </div>
            <div className="border-line2" style={{ width: '80%', borderTop: '3px solid #F3F4F8', borderRadius: '2px', marginTop: '20px', marginBottom: '15px' }}></div>
            <div className="Graphoutside" style={{ color: '#ffffff', backgroundColor: '#ffffff', width: 390, borderRadius: '10px', height: 280, flexDirection: 'column', justifyContent: 'center', alignItems: 'center', gap: 5, display: 'inline-flex' }}>
    <div className="Graph" style={{ width: 340, height: 240.65, position: 'relative', display: 'flex', flexDirection: 'column', justifyContent: 'flex-end', alignItems: 'center' }}>
        <div className="graphname" style={{ alignSelf: 'stretch', justifyContent: 'flex-start', alignItems: 'center', gap: 13, display: 'inline-flex', marginLeft: 10.5, marginTop: 10, marginBottom:10}}>
            <FontAwesomeIcon icon={faChartSimple} style={{ color: '#000000', fontSize: 24, fontWeight: 200 }} />
            <div style={{ width: 130, textAlign: 'center', color: '#2E2E30', fontSize: 24, fontFamily: 'Noto Sans KR', fontWeight: '700', wordWrap: 'break-word' }}>주간 그래프</div>
        </div>
        <div className='rectnagle-container' style={{ width: '90%', height: '200px', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end' }}>
            <div className="Rectangle2" style={{ width: 20.77, height: 68.20, background: '#7083FF', borderRadius: 10 }} />
            <div className="Rectangle3" style={{ width: 20.77, height: 116.82, background: '#7083FF', borderRadius: 10 }} />
            <div className="Rectangle4" style={{ width: 20.77, height: 41.42, background: '#7083FF', borderRadius: 10 }} />
            <div className="Rectangle5" style={{ width: 20.77, height: 140.33, background: '#7083FF', borderRadius: 10 }} />
            <div className="Rectangle6" style={{ width: 20.77, height: 101.82, background: '#7083FF', borderRadius: 10 }} />
            <div className="Rectangle7" style={{ width: 20.77, height: 101.82, background: '#7083FF', borderRadius: 10 }} />
            <div className="Rectangle8" style={{ width: 20.77, height: 101.82, background: '#D3D4FF', borderRadius: 10 }} />
        </div>
        <div className='week-container' style={{ width: '90%', display: 'flex', justifyContent: 'space-between', marginTop: '10px' }}>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>월</div>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>화</div>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>수</div>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>목</div>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>금</div>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>토</div>
            <div style={{ width: 15.58, textAlign: 'center', color: '#767676', fontSize: 14, fontFamily: 'Noto Sans KR', fontWeight: '500', wordWrap: 'break-word' }}>일</div>
        </div>
    </div>
</div>
        </div>
    );
};

export default State3;