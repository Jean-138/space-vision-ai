# Space Vision AI

API that analyzes space images using Artificial Intelligence and Computer Vision.

## What it does

You send an image of a space object (planet, nebula, galaxy, etc) and the API returns:

- Object identification
- Detailed description
- Simple explanation (educational)
- Basic scientific information

## Stack

- **FastAPI** - Web framework
- **OpenCV** - Image processing
- **Google Gemini** - AI analysis
- **Python 3.13**

## Installation

1. Clone the repository
```bash
git clone https://github.com/Jean-138/space-vision-ai.git
cd space-vision-ai
```

2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up Gemini API key
- Go to https://aistudio.google.com/app/apikey
- Create an API key
- Create a `.env` file in the root with:
GEMINI_API_KEY=your_key_here

## How to use

1. Start the server
```bash
uvicorn app.main:app --reload
```

2. Access the documentation
http://localhost:8000/docs

3. Use the `/analyze` endpoint to send an image

## Example response

```json
{
  "object_identified": "Orion Nebula",
  "description": "A giant interstellar cloud and H II region...",
  "simple_explanation": "It's like a cosmic factory where new stars are being born...",
  "scientific_info": "Located 1,344 light-years away, it's an emission nebula in the constellation Orion"
}
```

## Author

Jean - GitHub: [@Jean-138](https://github.com/Jean-138)

## License

MIT
