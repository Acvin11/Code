import React from 'react';
import ReactDOM from 'react-dom';
//import './index.css';
//import App from './App';
//import reportWebVitals from './reportWebVitals';

// ReactDOM.render(
//   <>
//       <div className="cards">
//         <div className="card">
//           <img src="" alt="myPic" className="card_img"></img>
//           <div className="card__info">
//              <span className="card__category">A NetFlix Originals</span>
//              <h3  className="card__title">Dark</h3>
//              <a href="" target="_blank">
//                   <button> WatchNow </button>
//              </a>
//           </div>
//         </div>
//       </div>
//   </>,
//   document.getElementById('root')
// );

const img1 = "https://picsum.photos/id/1/200/300";
ReactDOM.render(
  <>
      <h1 contentEditable="true" className="cards">Acvin Gonsalves</h1>
      <img src={img1} />
  </>,
  document.getElementById('root')
);
