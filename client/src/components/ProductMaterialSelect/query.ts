import { gql } from '@apollo/client';

const MATERIALS = gql`
  query {
    allMaterials {
      id
      name
    }
  }
`;

export default MATERIALS;
