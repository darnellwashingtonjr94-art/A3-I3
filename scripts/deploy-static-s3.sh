#!/bin/bash
BUCKET_NAME="my-sol-plex-bucket"
DISTRIBUTION_ID="E1XXXXXXX"
BUILD_DIR="./build" 

echo "Installing dependencies and building the project..."
npm install
npm run build 

echo "Syncing files to AWS S3..."
aws s3 sync $BUILD_DIR s3://$BUCKET_NAME --delete

echo "Invalidating CloudFront cache to serve the latest v0.1.5 release..."
aws cloudfront create-invalidation \
  --distribution-id $DISTRIBUTION_ID \
  --paths "/*"

echo "Deployment Complete!"
