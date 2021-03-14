import { gql } from '@apollo/client';

const CATEGORIES = gql`
  query {
    allCategories {
      id
      name
    }
  }
`;

export default CATEGORIES;
