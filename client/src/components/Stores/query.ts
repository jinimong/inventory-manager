import { gql } from '@apollo/client';

const STORES = gql`
  query {
    allStores {
      id
      name
    }
  }
`;

export default STORES;
