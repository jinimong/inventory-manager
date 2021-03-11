import React, { useState } from 'react';
import { gql, useMutation } from '@apollo/client';
import query from './Stores/query';

const CREATE_STORE = gql`
  mutation CreateStore($name: String!) {
    createStore(name: $name) {
      store {
        id
      }
    }
  }
`;

const CreateStore: React.FC = () => {
  const [state, setState] = useState({ name: '' });
  const { name } = state;
  const [createStore] = useMutation(CREATE_STORE);
  return (
    <form
      onSubmit={async (e) => {
        e.preventDefault();
        await createStore({
          variables: { name },
          refetchQueries: [{ query }],
        });
        setState({ name: '' });
      }}
    >
      <input
        placeholder="입점처 이름"
        value={state.name}
        onChange={(e) =>
          setState((prevState) => ({
            ...prevState,
            name: e.target.value,
          }))
        }
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateStore;
