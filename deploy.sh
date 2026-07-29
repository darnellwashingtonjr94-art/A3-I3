#!/bin/bash
set -e

# Colors for terminal output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}[*] Validating environment...${NC}"
if ! command -v vercel &> /dev/null
then
    echo "Error: Vercel CLI could not be found. Please run 'npm i -g vercel'"
    exit 1
fi

if [ "$1" == "--dev" ]; then
    echo -e "${GREEN}[*] Booting Vercel local development server...${NC}"
    vercel dev
else
    echo -e "${BLUE}[*] Initiating production deployment to Vercel...${NC}"
    # Deploy bypassing prompts for a strict CI-like push
    vercel --prod --yes
    echo -e "${GREEN}[*] Deployment sequence completed successfully.${NC}"
fi
