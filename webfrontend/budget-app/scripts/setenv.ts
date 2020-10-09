const { writeFile } = require('fs');
const { argv } = require('yargs');

// read environment variables from .env file
require('dotenv').config();

// read the command line arguments passed with yargs
const environment = argv.environment;
const isProduction = environment === 'prod';
const isDocker = environment === 'dev-docker';
const targetPath = isProduction
   ? `./src/environments/environment.prod.ts`
   : `./src/environments/environment.ts`;
let apiEndpoint = '';
if(isProduction) {
  apiEndpoint = process.env.PROD_API_ENDPOINT
} else if(isDocker) {
  apiEndpoint = process.env.DOCKER_API_ENDPOINT
} else {
  // debug dev
  apiEndpoint = process.env.DEBUG_API_ENDPOINT
}

// we have access to our environment variables
// in the process.env object thanks to dotenv
const environmentFileContent = `
export const environment = {
   production: ${isProduction},
   CLIENT_ID: "${process.env.CLIENT_ID}",
   CLIENT_SECRET: "${process.env.CLIENT_SECRET}",
   API_ENDPOINT: "${apiEndpoint}"
};
`;
// write the content to the respective file
writeFile(targetPath, environmentFileContent, function (err) {
   if (err) {
      console.log(err);
   }
   console.log(`Wrote variables to ${targetPath}`);
});
