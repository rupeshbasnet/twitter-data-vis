import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import './component.css';
import BarChart from './BarChart';

class Main extends React.Component {
   render() {
   return (
      <div>

      <div className= "container form">
      <nav className = "navbar navbar-expand-lg">
          <ul className = "navbar-nav">
            <li className = "nav-item">
				        Mode
            </li>
            <li className = "nav-item">
                Language
            </li>
            <li className = "nav-item">
                Interactions
            </li>
            <li className = "nav-item">
                Source
            </li>
            <li className = "nav-item">
                All Tweets
            </li>
          </ul>
        </nav>
      </div>

      <div>
      <BarChart data={[5,10,1,13,6,3,7,8,4,7,7,6]} size={[800,600]} />
      </div>

      </div>
   );
   }
}
export default Main
