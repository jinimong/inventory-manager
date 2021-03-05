import React from 'react';
import { HashRouter as Router, Route } from 'react-router-dom';
import EventDetail from './EventDetail';
import Events from './Events';
import Home from './Home';
import ProductDetail from './ProductDetail';
import Products from './Products';

function App() {
  return (
    <Router>
      <Route exact path="/" component={Home} />
      <Route exact path="/events" component={Events} />
      <Route exact path="/events/:id" component={EventDetail} />
      <Route exact path="/products" component={Products} />
      <Route exact path="/products/:id" component={ProductDetail} />
    </Router>
  );
}

export default App;
