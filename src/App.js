import './App.css';
import {Route, BrowserRouter as Router} from 'react-router-dom';

import Home from './screens/Home';
import StockData from './screens/StockData';

function App() {
  return (
    <Router>
      <div>
        <view></view>
        <Route path='/' exact component={Home} />
        <Route path='/StockData' component={StockData} />
      </div>
    </Router>
  );
}

export default App;
