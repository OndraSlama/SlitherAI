worldWidth = 1000
worldHeight = 1000
pixelScale = 5

windowWidth = 1200
windowHeight = 800

zoomStep = 0.1
maxZoom = 5
minZoom = 0.01

regionSize = 150 #Region size in world units (side of the square)
foodInRegion = 25 #Average number of food globes in region
foodNutritions = 12 #Average nutrition per food globe
resetFoodInterval = 60 #Every X second check of enough food

snakeInitialLength = 10000
greedFactor = 1.026 #Every new part of snakes body will cost times greeFactor more then previous
sizeGrowFactor = 1.02 #How much snake grows when new part added
sprintCost = 15 #Cost of sprinting per second (length/second)
turningAngle = 360 #How sharp turn can snake take in 1 second
snakeSpeed = 20 #Base speed of the snake (units/second)