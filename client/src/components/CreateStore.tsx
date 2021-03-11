import React from 'react';
import { gql, useMutation } from '@apollo/client';
import { useForm } from 'react-hook-form';
import query from './Stores/query';

type StoreInput = {
  name: string;
};

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
  const defaultValues = { name: '' };
  const [createStore] = useMutation(CREATE_STORE);

  // eslint-disable-next-line @typescript-eslint/unbound-method
  const { register, handleSubmit, reset } = useForm<StoreInput>({
    defaultValues,
  });
  const onSubmit = (formData: StoreInput) =>
    createStore({
      variables: { ...formData },
      refetchQueries: [{ query }],
    }).then(() => reset());
  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input placeholder="입점처 이름" name="name" ref={register} />
      <button type="submit">Submit</button>
    </form>
  );
};

export default CreateStore;
