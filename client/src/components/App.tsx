import { ApolloProvider } from '@apollo/client';
import React from 'react';
import { HashRouter as Router, Route, Switch } from 'react-router-dom';
import client from '../graphql/apollo';
import CreateEvent from './CreateEvent';
import CreateProduct from './CreateProduct';
import CreateStore from './CreateStore';
import EventDetail from './EventDetail';
import Events from './Events';
import Home from './Home';
import ProductDetail from './ProductDetail';
import Products from './Products';
import StoreDetail from './StoreDetail';
import Stores from './Stores';

const App: React.FC = () => {
  return (
    <ApolloProvider client={client}>
      <Router>
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/events" component={Events} />
          <Route exact path="/events/new" component={CreateEvent} />
          <Route exact path="/events/:id" component={EventDetail} />
          <Route exact path="/products" component={Products} />
          <Route exact path="/products/new" component={CreateProduct} />
          <Route exact path="/products/:id" component={ProductDetail} />
          <Route exact path="/stores" component={Stores} />
          <Route exact path="/stores/new" component={CreateStore} />
          <Route exact path="/stores/:id" component={StoreDetail} />
        </Switch>
      </Router>
    </ApolloProvider>
  );
};

export default App;
