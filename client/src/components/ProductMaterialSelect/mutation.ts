import { gql } from '@apollo/client';

const CREATE_MATERIAL = gql`
  mutation CreateProductMaterial($name: String!) {
    createMaterial(name: $name) {
      material {
        id
      }
    }
  }
`;

export default CREATE_MATERIAL;
