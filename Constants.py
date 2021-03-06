worldWidth = 1000
worldHeight = 1000
pixelScale = 5

windowWidth = 1200
windowHeight = 800

zoomStep = 0.1
maxZoom = 5
minZoom = 0.01
maxGameSpeed = 30
minGameSpeed = 1
showBotView = False

regionSize = 200 #Region size in world units (side of the square)
foodInRegion = 35 #Average number of food globes in region
foodNutritions = 16 #Average nutrition per food globe
resetFoodInterval = 30 #Every X second check of enough food
numberOfSnakes = 20

snakeInitialLength = 100
greedFactor = 1.046 #Every new part of snakes body will cost times greeFactor more then previous
sizeGrowFactor = 1.03 #How much snake grows when new part added
sprintCost = 15 #Cost of sprinting per second (length/second)
turningAngle = 360 #How sharp turn can snake take in 1 second
snakeSpeed = 20 #Base speed of the snake (units/second)

# Sensors
numberOfBeams = 5
numberOfSenses = 3
beamLength = 40
sideBeamAngle = 40
senseLength = 25

# GA
isHumanPlayer = True
training = True
loadFromFile = True
generationTimeLimit = 60*30 # game sec
hungerTimeLimit = 30
noOfSnakesLimit = 3
mutationRate = 0.08
surviveRatio = 0.35