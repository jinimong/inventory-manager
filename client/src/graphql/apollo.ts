import { ApolloClient, InMemoryCache } from '@apollo/client';
import { createUploadLink } from 'apollo-upload-client';

export const serverURL = 'http://localhost:8000';
const client = new ApolloClient({
  link: createUploadLink({ uri: `${serverURL}/graphql/` }),
  cache: new InMemoryCache(),
  resolvers: {},
});

export default client;
