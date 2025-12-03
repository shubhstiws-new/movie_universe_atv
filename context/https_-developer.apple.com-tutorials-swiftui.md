<!--
Downloaded via https://llm.codes by @steipete on December 1, 2025 at 08:58 PM
Source URL: https://developer.apple.com/tutorials/swiftui
Total pages processed: 11
URLs filtered: Yes
Content de-duplicated: Yes
Availability strings filtered: Yes
Code blocks only: No
-->

# https://developer.apple.com/tutorials/swiftui

# Introducing SwiftUI

SwiftUI is a modern way to declare user interfaces for any Apple platform. Create beautiful, dynamic apps faster than ever before.

**4hr 25min** Estimated Time

Get started

## Chapter 1 SwiftUI essentials

Learn how to use SwiftUI to compose rich views out of simple ones, set up data flow, and build the navigation while watching it unfold in Xcode’s preview.

1. Creating and combining views\\
\\
40min
2. Building lists and navigation\\
\\
35min
3. Handling user input\\
\\
20min

## Chapter 2 Drawing and animation

Discover how to draw shapes and paths to create a badge that you’ll animate, while also creating seamless transitions between views.

1. Drawing paths and shapes\\
\\
25min
2. Animating views and transitions\\
\\
20min

## Chapter 3 App design and layout

Explore the structure and layout of more complex interfaces built with SwiftUI.

1. Composing complex interfaces\\
\\
20min
2. Working with UI controls\\
\\
25min

## Chapter 4 Framework integration

Use SwiftUI views together with the views and view controllers from platform-specific UI frameworks.

1. Interfacing with UIKit\\
\\
25min
2. Creating a watchOS app\\
\\
25min
3. Creating a macOS app\\
\\
30min

## Resources

Explore more resources for learning about creating amazing apps with SwiftUI.

Documentation

Browse and search detailed API documentation.

- View fundamentals

- App organization

- Model data

View more

Videos

Watch WWDC sessions about SwiftUI.

- Introduction to SwiftUI

- What’s New in SwiftUI

- App Essentials in SwiftUI

Watch videos

Forums

Discuss SwiftUI with Apple engineers and other developers.

View forums

Sample Code

Download and explore sample code projects to get to know SwiftUI.

- Hello World

- Backyard Birds: Building an app with SwiftData and widgets

- Add rich graphics to your SwiftUI app

- Creating accessible views

Xcode and SDKs

Download Xcode 15 or later for the latest tools and SDKs.

View downloads

---

# https://developer.apple.com/tutorials/swiftui/drawing-paths-and-shapes

Drawing and animation

# Drawing paths and shapes

Users receive a badge whenever they visit a landmark in their list. Of course, for a user to receive a badge, you’ll need to create one. This tutorial takes you through the process of creating a badge by combining paths and shapes, which you then overlay with another shape that represents the location.

If you want to create multiple badges for different kinds of landmarks, try experimenting with the overlaid symbol, varying the amount of repetition, or changing the various angles and scales.

Follow the steps to build this project, or download the finished project to explore on your own.

25

mins

Section 1

## Create drawing data for a badge view

To create the badge, you’ll start by defining data that you can use to draw a hexagon shape for the badge’s background.

Step 1

Step 2

Name the new file `HexagonParameters.swift`.

You’ll use this structure to define the shape of a hexagon.

Step 3

Inside the new file, create a structure called `HexagonParameters`.

HexagonParameters.swift

import Foundation

struct HexagonParameters {
}

No Preview

Step 4

Define a `Segment` structure to hold the three points that represent one side of the hexagon; import `CoreGraphics` so you can use `CGPoint`.

Each side starts where the previous ends, moves in a straight line to the first point, and then moves over a Bézier curve at the corner to the second point. The third point controls the shape of the curve.

import CoreGraphics

struct HexagonParameters {
struct Segment {
let line: CGPoint
let curve: CGPoint
let control: CGPoint
}
}

struct HexagonParameters {

Step 5

Create an array to hold segments.

struct HexagonParameters {
struct Segment {
let line: CGPoint
let curve: CGPoint
let control: CGPoint
}

static let segments = [\
]
}

let control: CGPoint
}

Step 6

Add data for the six segments, one for each side of the hexagon.

The values are stored as a fraction of a unit square having its origin in the upper left, with positive x to the right and positive y down. Later, you’ll use these fractions to find the actual points of a hexagon with a given size.

static let segments = [\
Segment(\
line: CGPoint(x: 0.60, y: 0.05),\
curve: CGPoint(x: 0.40, y: 0.05),\
control: CGPoint(x: 0.50, y: 0.00)\
),\
Segment(\
line: CGPoint(x: 0.05, y: 0.20),\
curve: CGPoint(x: 0.00, y: 0.30),\
control: CGPoint(x: 0.00, y: 0.25)\
),\
Segment(\
line: CGPoint(x: 0.00, y: 0.70),\
curve: CGPoint(x: 0.05, y: 0.80),\
control: CGPoint(x: 0.00, y: 0.75)\
),\
Segment(\
line: CGPoint(x: 0.40, y: 0.95),\
curve: CGPoint(x: 0.60, y: 0.95),\
control: CGPoint(x: 0.50, y: 1.00)\
),\
Segment(\
line: CGPoint(x: 0.95, y: 0.80),\
curve: CGPoint(x: 1.00, y: 0.70),\
control: CGPoint(x: 1.00, y: 0.75)\
),\
Segment(\
line: CGPoint(x: 1.00, y: 0.30),\
curve: CGPoint(x: 0.95, y: 0.20),\
control: CGPoint(x: 1.00, y: 0.25)\
)\
]
}

Step 7

Add an adjustment value that lets you tune the shape of the hexagon.

static let adjustment: CGFloat = 0.085

static let segments = [\
Segment(\
line: CGPoint(x: 0.60, y: 0.05),\
curve: CGPoint(x: 0.40, y: 0.05),\
control: CGPoint(x: 0.50, y: 0.00)\
),\
Segment(\
line: CGPoint(x: 0.05, y: 0.20 + adjustment),\
curve: CGPoint(x: 0.00, y: 0.30 + adjustment),\
control: CGPoint(x: 0.00, y: 0.25 + adjustment)\
),\
Segment(\
line: CGPoint(x: 0.00, y: 0.70 - adjustment),\
curve: CGPoint(x: 0.05, y: 0.80 - adjustment),\
control: CGPoint(x: 0.00, y: 0.75 - adjustment)\
),\
Segment(\
line: CGPoint(x: 0.40, y: 0.95),\
curve: CGPoint(x: 0.60, y: 0.95),\
control: CGPoint(x: 0.50, y: 1.00)\
),\
Segment(\
line: CGPoint(x: 0.95, y: 0.80 - adjustment),\
curve: CGPoint(x: 1.00, y: 0.70 - adjustment),\
control: CGPoint(x: 1.00, y: 0.75 - adjustment)\
),\
Segment(\
line: CGPoint(x: 1.00, y: 0.30 + adjustment),\
curve: CGPoint(x: 0.95, y: 0.20 + adjustment),\
control: CGPoint(x: 1.00, y: 0.25 + adjustment)\
)\
]
}

}

static let segments = \
Segment(\
```\
\
No Preview\
\

\
[Section 2\
\
## Draw the badge background\
\
Use the graphics APIs in SwiftUI to draw a custom badge shape.\
\

\
Step 1\
\

\

\
Step 2\
\
In `BadgeBackground`, add a `Path` shape to the badge and apply the `fill()` modifier to turn the shape into a view.\
\
You use paths to combine lines, curves, and other drawing primitives to form more complex shapes like the badge’s hexagonal background.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
Path { path in\
\
}\
.fill(.black)\
}\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
struct BadgeBackground: View {\
var body: some View {\
Path { path in\
\
}\
.fill(.black)\
}\
}\
```\
\
No Preview\
\
Step 3\
\
Add a starting point to the path, assuming a container with size 100 x 100 px.\
\
The `move(to:)` method moves the drawing cursor within the bounds of a shape as though an imaginary pen or pencil is hovering over the area, waiting to start drawing.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
Path { path in\
var width: CGFloat = 100.0\
let height = width\
path.move(\
to: CGPoint(\
x: width * 0.95,\
y: height * 0.20\
)\
)\
}\
.fill(.black)\
}\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
var body: some View {\
Path { path in\
var width: CGFloat = 100.0\
let height = width\
path.move(\
to: CGPoint(\
x: width * 0.95,\
y: height * 0.20\
)\
)\
}\
.fill(.black)\
```\
\
No Preview\
\
Step 4\
\
Draw the lines for each point of the shape data to create a rough hexagonal shape.\
\
The `addLine(to:)` method takes a single point and draws it. Successive calls to `addLine(to:)` begin a line at the previous point and continue to the new point.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
Path { path in\
var width: CGFloat = 100.0\
let height = width\
path.move(\
to: CGPoint(\
x: width * 0.95,\
y: height * 0.20\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x,\
y: height * segment.line.y\
)\
)\
}\
}\
.fill(.black)\
}\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x,\
y: height * segment.line.y\
)\
)\
}\
}\
.fill(.black)\
```\
\
Preview\
\
Preview\
\

\
Don’t worry if your hexagon looks a little unusual; that’s because you’re ignoring the curved part of each segment at the shape’s corners. You’ll account for that next.\
\
Step 5\
\
Use the `addQuadCurve(to:control:)` method to draw the Bézier curves for the badge’s corners.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
Path { path in\
var width: CGFloat = 100.0\
let height = width\
path.move(\
to: CGPoint(\
x: width * 0.95,\
y: height * (0.20 + HexagonParameters.adjustment)\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x,\
y: height * segment.line.y\
)\
)\
\
path.addQuadCurve(\
to: CGPoint(\
x: width * segment.curve.x,\
y: height * segment.curve.y\
),\
control: CGPoint(\
x: width * segment.control.x,\
y: height * segment.control.y\
)\
)\
}\
}\
.fill(.black)\
}\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
to: CGPoint(\
x: width * 0.95,\
y: height * (0.20 + HexagonParameters.adjustment)\
)\
)\
```\
\
Preview\
\
Preview\
\

\
Step 6\
\
Wrap the path in a `GeometryReader` so the badge can use the size of its containing view, which defines the size instead of hard-coding the value (`100`).\
\
Using the smallest of the geometry’s two dimensions preserves the aspect ratio of the badge when its containing view isn’t square.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
var width: CGFloat = min(geometry.size.width, geometry.size.height)\
let height = width\
path.move(\
to: CGPoint(\
x: width * 0.95,\
y: height * (0.20 + HexagonParameters.adjustment)\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x,\
y: height * segment.line.y\
)\
)\
\
path.addQuadCurve(\
to: CGPoint(\
x: width * segment.curve.x,\
y: height * segment.curve.y\
),\
control: CGPoint(\
x: width * segment.control.x,\
y: height * segment.control.y\
)\
)\
}\
}\
.fill(.black)\
}\
}\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
struct BadgeBackground: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
var width: CGFloat = min(geometry.size.width, geometry.size.height)\
```\
\
Preview\
\
Preview\
\

\
Step 7\
\
Scale the shape on the x-axis using `xScale`, and then add `xOffset` to recenter the shape within its geometry.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
var width: CGFloat = min(geometry.size.width, geometry.size.height)\
let height = width\
let xScale: CGFloat = 0.832\
let xOffset = (width * (1.0 - xScale)) / 2.0\
width *= xScale\
path.move(\
to: CGPoint(\
x: width * 0.95 + xOffset,\
y: height * (0.20 + HexagonParameters.adjustment)\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x + xOffset,\
y: height * segment.line.y\
)\
)\
\
path.addQuadCurve(\
to: CGPoint(\
x: width * segment.curve.x + xOffset,\
y: height * segment.curve.y\
),\
control: CGPoint(\
x: width * segment.control.x + xOffset,\
y: height * segment.control.y\
)\
)\
}\
}\
.fill(.black)\
}\
}\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
var width: CGFloat = min(geometry.size.width, geometry.size.height)\
let height = width\
let xScale: CGFloat = 0.832\
let xOffset = (width * (1.0 - xScale)) / 2.0\
width *= xScale\
path.move(\
to: CGPoint(\
```\
\
Preview\
\
Preview\
\

\
Step 8\
\
Replace the solid black background with a gradient to match the design.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
var width: CGFloat = min(geometry.size.width, geometry.size.height)\
let height = width\
let xScale: CGFloat = 0.832\
let xOffset = (width * (1.0 - xScale)) / 2.0\
width *= xScale\
path.move(\
to: CGPoint(\
x: width * 0.95 + xOffset,\
y: height * (0.20 + HexagonParameters.adjustment)\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x + xOffset,\
y: height * segment.line.y\
)\
)\
\
path.addQuadCurve(\
to: CGPoint(\
x: width * segment.curve.x + xOffset,\
y: height * segment.curve.y\
),\
control: CGPoint(\
x: width * segment.control.x + xOffset,\
y: height * segment.control.y\
)\
)\
}\
}\
.fill(.linearGradient(\
Gradient(colors: [Self.gradientStart, Self.gradientEnd]),\
startPoint: UnitPoint(x: 0.5, y: 0),\
endPoint: UnitPoint(x: 0.5, y: 0.6)\
))\
}\
}\
static let gradientStart = Color(red: 239.0 / 255, green: 120.0 / 255, blue: 221.0 / 255)\
static let gradientEnd = Color(red: 239.0 / 255, green: 172.0 / 255, blue: 120.0 / 255)\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
}\
}\
.fill(.linearGradient(\
Gradient(colors: [Self.gradientStart, Self.gradientEnd]),\
startPoint: UnitPoint(x: 0.5, y: 0),\
endPoint: UnitPoint(x: 0.5, y: 0.6)\
))\
}\
}\
```\
\
Preview\
\
Preview\
\

\
Step 9\
\
Apply the `aspectRatio(_:contentMode:)` modifier to the gradient fill.\
\
By preserving a 1:1 aspect ratio, the badge maintains its position at the center of the view, even if its ancestor views aren’t square.\
\
BadgeBackground.swift\
\
```\
import SwiftUI\
\
struct BadgeBackground: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
var width: CGFloat = min(geometry.size.width, geometry.size.height)\
let height = width\
let xScale: CGFloat = 0.832\
let xOffset = (width * (1.0 - xScale)) / 2.0\
width *= xScale\
path.move(\
to: CGPoint(\
x: width * 0.95 + xOffset,\
y: height * (0.20 + HexagonParameters.adjustment)\
)\
)\
\
HexagonParameters.segments.forEach { segment in\
path.addLine(\
to: CGPoint(\
x: width * segment.line.x + xOffset,\
y: height * segment.line.y\
)\
)\
\
path.addQuadCurve(\
to: CGPoint(\
x: width * segment.curve.x + xOffset,\
y: height * segment.curve.y\
),\
control: CGPoint(\
x: width * segment.control.x + xOffset,\
y: height * segment.control.y\
)\
)\
}\
}\
.fill(.linearGradient(\
Gradient(colors: [Self.gradientStart, Self.gradientEnd]),\
startPoint: UnitPoint(x: 0.5, y: 0),\
endPoint: UnitPoint(x: 0.5, y: 0.6)\
))\
}\
.aspectRatio(1, contentMode: .fit)\
}\
static let gradientStart = Color(red: 239.0 / 255, green: 120.0 / 255, blue: 221.0 / 255)\
static let gradientEnd = Color(red: 239.0 / 255, green: 172.0 / 255, blue: 120.0 / 255)\
}\
\
#Preview {\
BadgeBackground()\
}\
```\
\
BadgeBackground.swift\
\
```\
))\
}\
.aspectRatio(1, contentMode: .fit)\
}\
static let gradientStart = Color(red: 239.0 / 255, green: 120.0 / 255, blue: 221.0 / 255)\
```\
\
Preview\
\
Preview\
\

\
Section 3\
\
## Draw the badge symbol\
\
The Landmarks badge has a custom insignia in its center that’s based on the mountain that appears in the Landmarks app icon.\
\
The mountain symbol consists of two shapes: one that represents a snowcap at the peak, and the other that represents vegetation along the approach. You’ll draw them using two partially triangular shapes that are set apart by a small gap.\
\

\
First you’ll give your app an icon, to establish a look for the badge.\
\
Step 1\
\
Navigate to the empty `AppIcon` item from your project’s Asset Catalog, and then drag the single png file from the downloaded projects’ `Resources` folder into the existing empty AppIcon set.\
\

\
Next, you’ll build the matching badge symbol.\
\
Step 2\
\
Create a new custom view called `BadgeSymbol` for the mountain shape that’s stamped in a rotated pattern in the badge design.\
\
BadgeSymbol.swift\
\
```\
import SwiftUI\
\
struct BadgeSymbol: View {\
var body: some View {\
Text("Hello, World!")\
}\
}\
\
#Preview {\
BadgeSymbol()\
}\
```\
\
BadgeSymbol.swift\
\
```\
import SwiftUI\
\
struct BadgeSymbol: View {\
var body: some View {\
Text("Hello, World!")\
}\
}\
\
#Preview {\
BadgeSymbol()\
}\
```\
\
No Preview\
\
Step 3\
\
Draw the top portion of the symbol using the path APIs.\
\
BadgeSymbol.swift\
\
```\
import SwiftUI\
\
struct BadgeSymbol: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
let width = min(geometry.size.width, geometry.size.height)\
let height = width * 0.75\
let spacing = width * 0.030\
let middle = width * 0.5\
let topWidth = width * 0.226\
let topHeight = height * 0.488\
\
path.addLines([\
CGPoint(x: middle, y: spacing),\
CGPoint(x: middle - topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing),\
CGPoint(x: middle + topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: spacing)\
])\
}\
}\
}\
}\
\
#Preview {\
BadgeSymbol()\
}\
```\
\
BadgeSymbol.swift\
\
```\
struct BadgeSymbol: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
let width = min(geometry.size.width, geometry.size.height)\
let height = width * 0.75\
let spacing = width * 0.030\
let middle = width * 0.5\
let topWidth = width * 0.226\
let topHeight = height * 0.488\
\
path.addLines([\
CGPoint(x: middle, y: spacing),\
CGPoint(x: middle - topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing),\
CGPoint(x: middle + topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: spacing)\
])\
}\
}\
}\
}\
```\
\
Preview\
\
Preview\
\

\
Step 4\
\
Draw the bottom portion of the symbol.\
\
Use the `move(to:)` modifier to insert a gap between multiple shapes in the same path.\
\
BadgeSymbol.swift\
\
```\
import SwiftUI\
\
struct BadgeSymbol: View {\
var body: some View {\
GeometryReader { geometry in\
Path { path in\
let width = min(geometry.size.width, geometry.size.height)\
let height = width * 0.75\
let spacing = width * 0.030\
let middle = width * 0.5\
let topWidth = width * 0.226\
let topHeight = height * 0.488\
\
path.addLines([\
CGPoint(x: middle, y: spacing),\
CGPoint(x: middle - topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing),\
CGPoint(x: middle + topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: spacing)\
])\
\
path.move(to: CGPoint(x: middle, y: topHeight / 2 + spacing * 3))\
path.addLines([\
CGPoint(x: middle - topWidth, y: topHeight + spacing),\
CGPoint(x: spacing, y: height - spacing),\
CGPoint(x: width - spacing, y: height - spacing),\
CGPoint(x: middle + topWidth, y: topHeight + spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing * 3)\
])\
}\
}\
}\
}\
\
#Preview {\
BadgeSymbol()\
}\
```\
\
BadgeSymbol.swift\
\
```\
CGPoint(x: middle, y: spacing)\
])

path.move(to: CGPoint(x: middle, y: topHeight / 2 + spacing * 3))
path.addLines([\
CGPoint(x: middle - topWidth, y: topHeight + spacing),\
CGPoint(x: spacing, y: height - spacing),\
CGPoint(x: width - spacing, y: height - spacing),\
CGPoint(x: middle + topWidth, y: topHeight + spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing * 3)\
])
}
}

Preview

Fill the symbol with the purple color from the design.

BadgeSymbol.swift

import SwiftUI

struct BadgeSymbol: View {
static let symbolColor = Color(red: 79.0 / 255, green: 79.0 / 255, blue: 191.0 / 255)

var body: some View {
GeometryReader { geometry in
Path { path in
let width = min(geometry.size.width, geometry.size.height)
let height = width * 0.75
let spacing = width * 0.030
let middle = width * 0.5
let topWidth = width * 0.226
let topHeight = height * 0.488

path.addLines([\
CGPoint(x: middle, y: spacing),\
CGPoint(x: middle - topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing),\
CGPoint(x: middle + topWidth, y: topHeight - spacing),\
CGPoint(x: middle, y: spacing)\
])

path.move(to: CGPoint(x: middle, y: topHeight / 2 + spacing * 3))
path.addLines([\
CGPoint(x: middle - topWidth, y: topHeight + spacing),\
CGPoint(x: spacing, y: height - spacing),\
CGPoint(x: width - spacing, y: height - spacing),\
CGPoint(x: middle + topWidth, y: topHeight + spacing),\
CGPoint(x: middle, y: topHeight / 2 + spacing * 3)\
])
}
.fill(Self.symbolColor)
}
}
}

#Preview {
BadgeSymbol()
}

var body: some View {
GeometryReader { geometry in

Create a new `RotatedBadgeSymbol` view to encapsulate the concept of a rotated symbol.

RotatedBadgeSymbol.swift

struct RotatedBadgeSymbol: View {
let angle: Angle

var body: some View {
BadgeSymbol()
.padding(-60)
.rotationEffect(angle, anchor: .bottom)
}
}

#Preview {
RotatedBadgeSymbol(angle: Angle(degrees: 5))
}

#Preview {

Section 4

## Combine the badge foreground and background

The badge design calls for the mountain shape to be rotated and repeated multiple times on top of the badge background.

Define a new type for rotation and leverage the `ForEach` view to apply the same adjustments to multiple copies of the mountain shape.

Create a new SwiftUI view called `Badge`.

Badge.swift

struct Badge: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
Badge()
}

#Preview {

Place `BadgeBackground` in the body of `Badge`.

struct Badge: View {
var body: some View {
BadgeBackground()
}
}

#Preview {

Lay the badge’s symbol over the badge background by placing it in a `ZStack`.

struct Badge: View {
var badgeSymbols: some View {
RotatedBadgeSymbol(angle: Angle(degrees: 0))
.opacity(0.5)
}

var body: some View {
ZStack {
BadgeBackground()

badgeSymbols
}
}
}

#Preview {

var body: some View {
ZStack {

As it appears now, the badge symbol is too large compared to the intended design and relative size of the background.

Correct the size of the badge symbol by reading the surrounding geometry and scaling the symbol.

GeometryReader { geometry in
badgeSymbols
.scaleEffect(1.0 / 4.0, anchor: .top)
.position(x: geometry.size.width / 2.0, y: (3.0 / 4.0) * geometry.size.height)
}
}
}
}

#Preview {

BadgeBackground()

GeometryReader { geometry in
badgeSymbols
.scaleEffect(1.0 / 4.0, anchor: .top)
.position(x: geometry.size.width / 2.0, y: (3.0 / 4.0) * geometry.size.height)
}
}
}

Add a `ForEach` view to rotate and display copies of the badge symbol.

A full, 360° rotation split into eight segments creates a sun-like pattern by repeating the mountain symbol.

struct Badge: View {
var badgeSymbols: some View {
ForEach(0..<8) { index in
RotatedBadgeSymbol(
angle: .degrees(Double(index) / Double(8)) * 360.0
)
}
.opacity(0.5)
}

GeometryReader { geometry in
badgeSymbols
.scaleEffect(1.0 / 4.0, anchor: .top)
.position(x: geometry.size.width / 2.0, y: (3.0 / 4.0) * geometry.size.height)
}
}
.scaledToFit()
}
}

#Preview {

To keep the project organized, before moving on to the next tutorial, collect all of the new files that you added in this tutorial into a Badges group.

#Preview {

## Check Your Understanding

Question 1 of 3

What is the purpose of `GeometryReader`?

Possible answers

You use `GeometryReader` to divide the parent view into a grid that you use to lay out views onscreen.

You use `GeometryReader` to dynamically draw, position, and size views instead of hard-coding numbers that might not be correct when you reuse a view somewhere else in your app, or on a different-sized display.

You use `GeometryReader` to automatically identify the type and position of shape views in your app’s view hierarchy, such as `Circle`.

Submit Next question

Next

## Animating views and transitions

When using SwiftUI, you can individually animate changes to views, or to a view’s state, no matter where the effects are. SwiftUI handles all the complexity of these combined, overlapping, and interruptible animations for you.

Get started

---

# https://developer.apple.com/tutorials/swiftui/composing-complex-interfaces

App design and layout

# Composing complex interfaces

The category view for Landmarks shows a vertically scrolling list of horizontally scrolling landmarks. As you build this view and connect it to your existing views, you’ll explore how composed views can adapt to different device sizes and orientations.

Follow the steps to build this project, or download the finished project to explore on your own.

20

mins

Section 1

## Add a category view

You can provide a different way to browse the landmarks by creating a view that sorts landmarks by category, while highlighting a featured landmark at the top of the view.

Step 1

Create a Categories group in your project’s Views group, and create a custom view called `CategoryHome` to the new group.

CategoryHome.swift

import SwiftUI

struct CategoryHome: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
CategoryHome()
}

#Preview {

Preview

Step 2

Add a `NavigationSplitView` to host the different categories.

You use navigation split views along with `NavigationLink` instances and related modifiers to build hierarchical navigation structures in your app.

struct CategoryHome: View {
var body: some View {
NavigationSplitView {
Text("Hello, World!")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

Step 3

Set the title of the navigation bar to Featured.

The view showcases one or more featured landmarks at the top.

struct CategoryHome: View {
var body: some View {
NavigationSplitView {
Text("Hello, World!")
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

NavigationSplitView {
Text("Hello, World!")
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")

#Preview {

Section 2

## Create a category list

The category view displays all categories in separate rows arranged in a vertical column for easier browsing. You do this by combining vertical and horizontal stacks, and adding scrolling to the list.

Start by reading category data from the `landmarkData.json` file.

In `Landmark`, add a `Category` enumeration and a `category` property to the `Landmark` structure.

The `landmarkData` file already includes a `category` value for each landmark with one of three string values. By matching the names in the data file, you can rely on the structure’s `Codable` conformance to load the data.

Landmark.swift

import Foundation
import SwiftUI
import CoreLocation

struct Landmark: Hashable, Codable, Identifiable {
var id: Int
var name: String
var park: String
var state: String
var description: String
var isFavorite: Bool

var category: Category
enum Category: String, CaseIterable, Codable {
case lakes = "Lakes"
case rivers = "Rivers"
case mountains = "Mountains"
}

private var imageName: String
var image: Image {
Image(imageName)
}

private var coordinates: Coordinates
var locationCoordinate: CLLocationCoordinate2D {
CLLocationCoordinate2D(
latitude: coordinates.latitude,
longitude: coordinates.longitude)
}

struct Coordinates: Hashable, Codable {
var latitude: Double
var longitude: Double
}
}

var isFavorite: Bool

private var imageName: String

No Preview

In `ModelData`, add a computed `categories` dictionary, with category names as keys, and an array of associated landmarks for each key.

ModelData.swift

import Foundation

@Observable
class ModelData {
var landmarks: [Landmark] = load("landmarkData.json")
var hikes: [Hike] = load("hikeData.json")

var categories: [String: [Landmark]] {
Dictionary(
grouping: landmarks,
by: { $0.category.rawValue }
)
}
}

let data: Data

guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
else {
fatalError("Couldn't find \(filename) in main bundle.")
}

do {
data = try Data(contentsOf: file)
} catch {
fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
}

do {
let decoder = JSONDecoder()
return try decoder.decode(T.self, from: data)
} catch {
fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
}
}

var hikes: [Hike] = load("hikeData.json")

In `CategoryHome`, create a `modelData` property.

You’ll need access to the categories right now, as well as to other landmark data later.

struct CategoryHome: View {
@Environment(ModelData.self) var modelData

var body: some View {
NavigationSplitView {
Text("Landmarks Content")
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {
CategoryHome()
.environment(ModelData())
}

var body: some View {

Step 4

Display the categories in Landmarks using a `List`.

The `Landmark.Category` case name identifies each item in the list, which must be unique among other categories because it’s an enumeration.

var body: some View {
NavigationSplitView {
List {
ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
Text(key)
}
}
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

var body: some View {
NavigationSplitView {
List {
ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
Text(key)
}
}
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")

Section 3

## Create a category row

Landmarks displays each category in a row that scrolls horizontally. Add a new view type to represent the row, then display all the landmarks for that category in the new view.

Reuse parts of the `Landmark` view you created in Creating and combining views to create familiar previews of a landmark.

Define a new custom view `CategoryRow` for holding the contents of a row.

CategoryRow.swift

struct CategoryRow: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
CategoryRow()
}

#Preview {

Add properties for the category name and the list of items in that category.

struct CategoryRow: View {
var categoryName: String
var items: [Landmark]

var body: some View {
Text("Hello, World!")
}
}

#Preview {
let landmarks = ModelData().landmarks
return CategoryRow(
categoryName: landmarks[0].category.rawValue,
items: Array(landmarks.prefix(3))
)
}

var body: some View {
Text("Hello, World!")

Display the name of the category.

var body: some View {
Text(categoryName)
.font(.headline)
}
}

#Preview {

Put the category’s items in an `HStack`, and group that with the category name in a `VStack`.

var body: some View {
VStack(alignment: .leading) {
Text(categoryName)
.font(.headline)

HStack(alignment: .top, spacing: 0) {
ForEach(items) { landmark in
Text(landmark.name)
}
}
}
}
}

#Preview {

Step 5

Give the content some space by specifying a tall `frame(width:height:)`, adding padding, and wrapping the `HStack` in a scroll view.

Updating the view preview with a larger sampling of data makes it easier to ensure that the scrolling behavior is correct.

var body: some View {
VStack(alignment: .leading) {
Text(categoryName)
.font(.headline)
.padding(.leading, 15)
.padding(.top, 5)

ScrollView(.horizontal, showsIndicators: false) {
HStack(alignment: .top, spacing: 0) {
ForEach(items) { landmark in
Text(landmark.name)
}
}
}
.frame(height: 185)
}
}
}

#Preview {
let landmarks = ModelData().landmarks
return CategoryRow(
categoryName: landmarks[0].category.rawValue,
items: Array(landmarks.prefix(4))
)
}

Text(categoryName)
.font(.headline)
.padding(.leading, 15)
.padding(.top, 5)

ScrollView(.horizontal, showsIndicators: false) {

Step 6

Create a new custom view called `CategoryItem` that displays one landmark.

CategoryItem.swift

struct CategoryItem: View {
var landmark: Landmark

var body: some View {
VStack(alignment: .leading) {
landmark.image
.resizable()
.frame(width: 155, height: 155)
.cornerRadius(5)
Text(landmark.name)
.font(.caption)
}
.padding(.leading, 15)
}
}

#Preview {
CategoryItem(landmark: ModelData().landmarks[0])
}

#Preview {

Step 7

In `CategoryRow`, replace the `Text` that holds the landmark name with the new `CategoryItem` view.

ScrollView(.horizontal, showsIndicators: false) {
HStack(alignment: .top, spacing: 0) {
ForEach(items) { landmark in
CategoryItem(landmark: landmark)
}
}
}
.frame(height: 185)
}
}
}

#Preview {

HStack(alignment: .top, spacing: 0) {
ForEach(items) { landmark in
CategoryItem(landmark: landmark)
}
}

#Preview {

Section 4

## Complete the category view

Add the rows and the featured image to the category home page.

Video with custom controls.

Content description: A flow diagram that shows how a location's image is composed to create the circular image mask.

Play

Update the body of `CategoryHome` to pass category information to instances of the row type.

var body: some View {
NavigationSplitView {
List {
ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
}
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

List {
ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
}

Next, you’ll add a featured landmark to the top of the view. You’ll need more information from the landmark data to do this.

In `Landmark`, add a new `isFeatured` property.

Like for other landmark properties you’ve added, this Boolean already exists in the data — you just need to declare a new property.

struct Landmark: Hashable, Codable, Identifiable {
var id: Int
var name: String
var park: String
var state: String
var description: String
var isFavorite: Bool
var isFeatured: Bool

var description: String
var isFavorite: Bool
var isFeatured: Bool

var category: Category

In `ModelData`, add a new computed `features` array, which contains only the landmarks that have `isFeatured` set to `true`.

var features: [Landmark] {
landmarks.filter { $0.isFeatured }
}

var categories: [String: [Landmark]] {
Dictionary(

In `CategoryHome`, add the image of the first featured landmark to the top of the list.

You’ll turn this view into an interactive carousel in a later tutorial. For now, it displays one of the featured landmarks with a scaled and cropped preview image.

var body: some View {
NavigationSplitView {
List {
modelData.features[0].image
.resizable()
.scaledToFill()
.frame(height: 200)
.clipped()

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
}
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

NavigationSplitView {
List {
modelData.features[0].image
.resizable()
.scaledToFill()
.frame(height: 200)
.clipped()

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)

Set the edge insets to zero on both kinds of landmark previews so the content can extend to the edges of the display.

var body: some View {
NavigationSplitView {
List {
modelData.features[0].image
.resizable()
.scaledToFill()
.frame(height: 200)
.clipped()
.listRowInsets(EdgeInsets())

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
.listRowInsets(EdgeInsets())
}
.navigationTitle("Featured")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

.frame(height: 200)
.clipped()
.listRowInsets(EdgeInsets())

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in

#Preview {

Section 5

## Add navigation between sections

With all of the differently categorized landmarks visible in the view, the user needs a way to reach each section in the app. Use the navigation and presentation APIs to make the category home, the detail view, and favorites list navigable from a tab view.

In `CategoryRow`, wrap the existing `CategoryItem` with a `NavigationLink`.

The category item itself is the label for the button, and its destination is the landmark detail view for the landmark represented by the card.

ScrollView(.horizontal, showsIndicators: false) {
HStack(alignment: .top, spacing: 0) {
ForEach(items) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
CategoryItem(landmark: landmark)
}
}
}
}
.frame(height: 185)
}
}
}

#Preview {

HStack(alignment: .top, spacing: 0) {
ForEach(items) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
CategoryItem(landmark: landmark)
}
}
}

Pin the preview so you can see the effect of the next step on the `CategoryRow`.

Change the navigation appearance of the category items by applying the `renderingMode(_:)` and `foregroundStyle(_:)` modifiers.

Text that you pass as the label for a navigation link renders using the environment’s accent color, and images may render as template images. You can modify either behavior to best suit your design.

var body: some View {
VStack(alignment: .leading) {
landmark.image
.renderingMode(.original)
.resizable()
.frame(width: 155, height: 155)
.cornerRadius(5)
Text(landmark.name)
.foregroundStyle(.primary)
.font(.caption)
}
.padding(.leading, 15)
}
}

#Preview {

VStack(alignment: .leading) {
landmark.image
.renderingMode(.original)
.resizable()
.frame(width: 155, height: 155)

Next you’ll modify the app’s main content view to show a tab view that lets the user choose between the category view you just created, and the existing list of landmarks.

Unpin the preview, switch to the `ContentView` and add an enumeration of the tabs to display.

ContentView.swift

struct ContentView: View {

enum Tab {
case featured
case list
}

var body: some View {
LandmarkList()
}
}

#Preview {
ContentView()
.environment(ModelData())
}

Add a state variable for the tab selection, and give it a default value.

struct ContentView: View {
@State private var selection: Tab = .featured

#Preview {

enum Tab {

Create a tab view that wraps the `LandmarkList`, as well as the new `CategoryHome`.

The `tag(_:)` modifier on each of the views matches one of the possible values that the `selection` property can take so the `TabView` can coordinate which view to display when the user makes a selection in the user interface.

var body: some View {
TabView(selection: $selection) {
CategoryHome()
.tag(Tab.featured)

LandmarkList()
.tag(Tab.list)
}
}
}

#Preview {

Give each tab a label.

var body: some View {
TabView(selection: $selection) {
CategoryHome()
.tabItem {
Label("Featured", systemImage: "star")
}
.tag(Tab.featured)

LandmarkList()
.tabItem {
Label("List", systemImage: "list.bullet")
}
.tag(Tab.list)
}
}
}

#Preview {

TabView(selection: $selection) {
CategoryHome()
.tabItem {
Label("Featured", systemImage: "star")
}
.tag(Tab.featured)

Make sure the Live preview is on and try out the new navigation.

Content description: A video showing the user tapping on one of the items in the category list to reveal the detail view, navigating back, and then choosing the List tab and navigating around the list view, before returning to the Featured tab.

#Preview {

## Check Your Understanding

Question 1 of 3

Which view is the root view for the Landmarks app?

Possible answers

`LandmarksApp`

`Landmarks`

`ContentView`

Submit Next question

Next

## Working with UI controls

In the Landmarks app, users can create a profile to express their personality. To give users the ability to change their profile, you’ll add an edit mode and design the preferences screen.

Get started

---

# https://developer.apple.com/tutorials/swiftui/creating-and-combining-views

SwiftUI essentials

# Creating and combining views

This tutorial guides you through building _Landmarks_ — an app for discovering and sharing the places you love. You’ll start by building the view that shows a landmark’s details.

To lay out the views, Landmarks uses _stacks_ to combine and layer the image and text view components. To add a map to the view, you’ll include a standard MapKit component. As you refine the view’s design, Xcode provides real-time feedback so you can see how those changes translate into code.

Download the project files to begin building this project, and follow the steps below.

40

mins

Section 1

## Create a new project and explore the canvas

Create a new Xcode project that uses SwiftUI. Explore the canvas, previews, and the SwiftUI template code.

To preview and interact with views from the canvas in Xcode, and to use all the latest features described throughout the tutorials, ensure your Mac is running macOS Sonoma or later.

Step 1

Step 2

In the template selector, select iOS as the platform, select the App template, and then click Next.

Step 3

Enter “Landmarks” as the product name, select “SwiftUI” for the interface and “Swift” for the language, and click Next. Choose a location to save the Landmarks project on your Mac.

Step 4

In the Project navigator, select `LandmarksApp`.

An app that uses the SwiftUI app life cycle has a structure that conforms to the `App` protocol. The structure’s `body` property returns one or more scenes, which in turn provide content for display. The `@main` attribute identifies the app’s entry point.

LandmarksApp.swift

import SwiftUI

@main
struct LandmarksApp: App {
var body: some Scene {
WindowGroup {
ContentView()
}
}
}

No Preview

Step 5

In the Project navigator, select `ContentView`.

By default, SwiftUI view files declare a structure and a preview. The structure conforms to the `View` protocol and describes the view’s content and layout. The preview declaration creates a preview for that view.

ContentView.swift

struct ContentView: View {
var body: some View {
VStack {
Image(systemName: "globe")
.imageScale(.large)
.foregroundStyle(.tint)
Text("Hello, world!")
}
.padding()
}
}

#Preview {
ContentView()
}

#Preview {

Preview

Step 6

The canvas displays a preview automatically.

Step 7

Inside the body property, remove everything but the `Text` declaration and change “Hello, world!” to a greeting for yourself.

As you change the code in a view’s `body` property, the preview updates to reflect your changes.

struct ContentView: View {
var body: some View {
Text("Hello SwiftUI!")
}
}

#Preview {

Section 2

## Customize the text view

You can customize a view’s display by changing your code, or by using the inspector to discover what’s available and to help you write code.

As you build the Landmarks app, you can use any combination of editors: the source editor, the canvas, or the inspectors. Your code stays updated, regardless of which tool you use.

Video with custom controls.

Play

Next, you’ll customize the text view using the inspector.

Change the canvas mode to Selectable.

The canvas displays previews in Live mode by default so that you can interact with them, but you can use the Selectable mode to enable editing instead.

In the preview, Command-Control-click the greeting to bring up the structured editing popover, and choose “Show SwiftUI Inspector”.

The popover shows different attributes that you can customize, depending on the type of view you inspect.

Use the inspector to change the text to “Turtle Rock”, the name of the first landmark you’ll show in your app.

Change the Font modifier to “Title”.

This applies the system font to the text so that it responds correctly to the user’s preferred font sizes and settings.

To customize a SwiftUI view, you call methods called _modifiers_. Modifiers wrap a view to change its display or other properties. Each modifier returns a new view, so it’s common to chain multiple modifiers, stacked vertically.

Edit the code by hand to add the `foregroundColor(.green)` modifier; this changes the text’s color to green.

struct ContentView: View {
var body: some View {
Text("Turtle Rock")
.font(.title)
.foregroundColor(.green)
}
}

#Preview {

Text("Turtle Rock")
.font(.title)
.foregroundColor(.green)
}
}

Your code is always the source of truth for the view. When you use the inspector to change or remove a modifier, Xcode updates your code immediately to match.

This time, open the inspector by Control-clicking on the `Text` declaration in the code editor, and then choose “Show SwiftUI Inspector” from the popover. Click the Color pop-up menu and choose Inherited to change the text color to black again.

Notice that Xcode updates your code automatically to reflect the change, removing the `foregroundColor(.green)` modifier.

struct ContentView: View {
var body: some View {
Text("Turtle Rock")
.font(.title)

}
}

#Preview {

Text("Turtle Rock")
.font(.title)

Step 8

Set the preview

Section 3

## Combine views using stacks

Beyond the title view you created in the previous section, you’ll add text views to contain details about the landmark, such as the name of the park and state it’s in.

When creating a SwiftUI view, you describe its content, layout, and behavior in the view’s `body` property; however, the `body` property only returns a single view. You can combine and embed multiple views in _stacks_, which group views together horizontally, vertically, or back-to-front.

In this section, you’ll use a vertical stack to place the title above a horizontal stack that contains details about the park.

You can use Xcode to embed a view in a container view, open an inspector, or help with other useful changes.

Control-click the text view’s initializer to show a context menu, and then choose “Embed in VStack”.

Next, you’ll add a text view to the stack by dragging a `Text` view from the library.

Open the library by clicking the plus button (+) at the top-right of the Xcode window, and then drag a `Text` view to the place in your code immediately below the “Turtle Rock” text view.

Replace the `Text` view’s placeholder text with “Joshua Tree National Park”.

struct ContentView: View {
var body: some View {
VStack {
Text("Turtle Rock")
.font(.title)
Text("Joshua Tree National Park")
}
}
}

#Preview {

Text("Turtle Rock")
.font(.title)
Text("Joshua Tree National Park")
}
}

Customize the location to match the desired layout.

Set the location’s font to `subheadline`.

struct ContentView: View {
var body: some View {
VStack {
Text("Turtle Rock")
.font(.title)
Text("Joshua Tree National Park")
.font(.subheadline)
}
}
}

#Preview {

.font(.title)
Text("Joshua Tree National Park")
.font(.subheadline)
}
}

Edit the `VStack` initializer to align the views by their leading edges.

By default, stacks center their contents along their axis and provide context-appropriate spacing.

struct ContentView: View {
var body: some View {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
Text("Joshua Tree National Park")
.font(.subheadline)
}
}
}

#Preview {

struct ContentView: View {
var body: some View {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)

Next, you’ll add another text view to the right of the location, this for the park’s state.

Embed the “Joshua Tree National Park” text view in an HStack.

struct ContentView: View {
var body: some View {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
}
}
}
}

#Preview {

Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
}
}
}

Add a new text view after the location, change the placeholder text to the park’s state, and then set its font to `subheadline`.

struct ContentView: View {
var body: some View {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Text("California")
.font(.subheadline)
}
}
}
}

#Preview {

Text("Joshua Tree National Park")
.font(.subheadline)
Text("California")
.font(.subheadline)
}
}

To direct the layout to use the full width of the device, separate the park and the state by adding a `Spacer` to the horizontal stack holding the two text views.

A _spacer_ expands to make its containing view use all of the space of its parent view, instead of having its size defined only by its contents.

struct ContentView: View {
var body: some View {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)
}
}
}
}

#Preview {

Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)

Step 9

Finally, use the `padding()` modifier to give the landmark’s name and details a little more space around their outer edges.

struct ContentView: View {
var body: some View {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)
}
}
.padding()
}
}

#Preview {

}
}
.padding()
}
}

Section 4

## Create a custom image view

With the name and location views all set, the next step is to add an image for the landmark.

Instead of adding more code in this file, you’ll create a custom view that applies a mask, border, and drop shadow to the image.

Start by adding an image to the project’s asset catalog.

Find `turtlerock@2x.jpg` in the project files’ Resources folder; drag it into the asset catalog’s editor. Xcode creates a new image set for the image.

Next, you’ll create a new SwiftUI view for your custom image view.

You’re ready to insert the image and modify its display to match the desired design.

Replace the text view with the image of Turtle Rock by using the `Image(_:)` initializer, passing it the name of the image to display.

CircleImage.swift

struct CircleImage: View {
var body: some View {
Image("turtlerock")
}
}

#Preview {
CircleImage()
}

Add a call to `clipShape(Circle())` to apply the circular clipping shape to the image.

The `Circle` type is a shape that you can use as a mask, or as a view by giving the circle a stroke or fill.

struct CircleImage: View {
var body: some View {
Image("turtlerock")
.clipShape(Circle())
}
}

#Preview {

var body: some View {
Image("turtlerock")
.clipShape(Circle())
}
}

Create another circle with a gray stroke, and then add it as an overlay to give the image a border.

struct CircleImage: View {
var body: some View {
Image("turtlerock")
.clipShape(Circle())
.overlay {
Circle().stroke(.gray, lineWidth: 4)
}
}
}

#Preview {

Image("turtlerock")
.clipShape(Circle())
.overlay {
Circle().stroke(.gray, lineWidth: 4)
}
}
}

Next, add a shadow with a 7 point radius.

struct CircleImage: View {
var body: some View {
Image("turtlerock")
.clipShape(Circle())
.overlay {
Circle().stroke(.gray, lineWidth: 4)
}
.shadow(radius: 7)
}
}

#Preview {

Circle().stroke(.gray, lineWidth: 4)
}
.shadow(radius: 7)
}
}

Switch the border color to white.

This completes the image view.

struct CircleImage: View {
var body: some View {
Image("turtlerock")
.clipShape(Circle())
.overlay {
Circle().stroke(.white, lineWidth: 4)
}
.shadow(radius: 7)
}
}

#Preview {

.clipShape(Circle())
.overlay {
Circle().stroke(.white, lineWidth: 4)
}
.shadow(radius: 7)

Section 5

## Use SwiftUI views from other frameworks

Next you’ll create a map that centers on a given coordinate. You can use the `Map` view from MapKit to render the map.

To get started, you’ll create a new custom view to manage your map.

Add an `import` statement for `MapKit`.

When you import SwiftUI and certain other frameworks in the same file, you gain access to SwiftUI-specific functionality provided by that framework.

MapView.swift

import SwiftUI
import MapKit

struct MapView: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
MapView()
}

struct MapView: View {

Create a private computed variable that holds the region information for the map.

struct MapView: View {
var body: some View {
Text("Hello, World!")
}

private var region: MKCoordinateRegion {
MKCoordinateRegion(
center: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868),
span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
)
}
}

#Preview {

Text("Hello, World!")
}

Replace the default `Text` view with a `Map` view that takes a camera position that you initialize with the region.

struct MapView: View {
var body: some View {
Map(initialPosition: .region(region))
}

#Preview {

You’ll see a map centered on Turtle Rock in the preview.

You can manipulate the map in live preview to zoom out a bit and see the surrounding area using the Option-click-drag control.

Section 6

## Compose the detail view

You now have all of the components you need — the name and place, a circular image, and a map for the location.

With the tools you’ve used so far, combine your custom views to create the final design for the landmark detail view.

In the Project navigator, select the `ContentView` file.

#Preview {

#Preview {

Embed the `VStack` that holds the three text views in another `VStack`.

struct ContentView: View {
var body: some View {
VStack {
VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)
}
}
.padding()
}
}
}

#Preview {

struct ContentView: View {
var body: some View {
VStack {
VStack(alignment: .leading) {
Text("Turtle Rock")

Add your custom `MapView` to the top of the stack. Set the size of the `MapView` with `frame(width:height:)`.

When you specify only the `height` parameter, the view automatically sizes to the width of its content. In this case, `MapView` expands to fill the available space.

struct ContentView: View {
var body: some View {
VStack {
MapView()
.frame(height: 300)

VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)
}
}
.padding()
}
}
}

#Preview {

var body: some View {
VStack {
MapView()
.frame(height: 300)

VStack(alignment: .leading) {
Text("Turtle Rock")

Add the `CircleImage` view to the stack.

CircleImage()

#Preview {

.frame(height: 300)

To layer the image view on top of the map view, give the image an offset of -130 points vertically, and padding of -130 points from the bottom of the view.

These adjustments make room for the text by moving the image upwards.

CircleImage()
.offset(y: -130)
.padding(.bottom, -130)

#Preview {

VStack(alignment: .leading) {

Add a spacer at the bottom of the outer `VStack` to push the content to the top of the screen.

VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)
}
}
.padding()

Spacer()
}
}
}

#Preview {

}
.padding()

Spacer()
}
}

Add a divider and some additional descriptive text for the landmark.

VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
.font(.subheadline)
Spacer()
Text("California")
.font(.subheadline)
}

Divider()

Text("About Turtle Rock")
.font(.title2)
Text("Descriptive text goes here.")
}
.padding()

#Preview {

.font(.subheadline)
}

Finally, move the subheadline font modifier from each `Text` view to the `HStack` containing them, and apply the secondary style to the subheadline text.

When you apply a modifier to a layout view like a stack, SwiftUI applies the modifier to all the elements contained in the group.

VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)
HStack {
Text("Joshua Tree National Park")
Spacer()
Text("California")
}
.font(.subheadline)
.foregroundStyle(.secondary)

#Preview {

Text("California")
}
.font(.subheadline)
.foregroundStyle(.secondary)

#Preview {

## Check Your Understanding

Question 1 of 4

When creating a custom SwiftUI view, where do you declare the view’s layout?

Possible answers

In the view’s initializer.

In the `body` property.

In the `layoutSubviews()` method.

Submit Next question

Next

## Building lists and navigation

With the basic landmark detail view set up, you need to provide a way for users to see the full list of landmarks, and to view the details about each location.

Get started

---

# https://developer.apple.com/tutorials/swiftui/animating-views-and-transitions

Drawing and animation

# Animating views and transitions

When using SwiftUI, you can individually animate changes to views, or to a view’s state, no matter where the effects are. SwiftUI handles all the complexity of these combined, overlapping, and interruptible animations for you.

In this tutorial, you’ll animate a view that contains a graph for tracking the hikes a user takes while using the Landmarks app. Using the `animation(_:)` modifier, you’ll see just how easy it is to animate a view.

Download the starter project and follow along with this tutorial, or open the finished project and explore the code on your own.

20

mins

Section 1

## Add hiking data to the app

Before you can add animation, you’ll need something to animate. In this section, you’ll import and model hiking data, and then add some prebuilt views for displaying that data statically in a graph.

Step 1

Drag the `hikeData.json` file from the downloaded files’ Resources folder into your project’s Resources group. Be sure to select “Copy items if needed” before clicking Finish.

Step 2

Like the `Landmark` structure, the `Hike` structure conforms to `Codable` and has properties that match the keys in the corresponding data file.

Hike.swift

import Foundation

struct Hike: Codable, Hashable, Identifiable {
var id: Int
var name: String
var distance: Double
var difficulty: Int
var observations: [Observation]

static var formatter = LengthFormatter()

var distanceText: String {
Hike.formatter
.string(fromValue: distance, unit: .kilometer)
}

struct Observation: Codable, Hashable {
var distanceFromStart: Double

}

No Preview

Step 3

Load the `hikes` array into your model.

ModelData.swift

@Observable
class ModelData {
var landmarks: [Landmark] = load("landmarkData.json")
var hikes: [Hike] = load("hikeData.json")
}

let data: Data

guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
else {
fatalError("Couldn't find \(filename) in main bundle.")
}

do {
data = try Data(contentsOf: file)
} catch {
fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
}

do {
let decoder = JSONDecoder()
return try decoder.decode(T.self, from: data)
} catch {
fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
}
}

class ModelData {
var landmarks: [Landmark] = load("landmarkData.json")
var hikes: [Hike] = load("hikeData.json")
}

Step 4

Drag the `Hikes` folder from the downloaded files’ Resources folder into your project’s Views group. Be sure to select “Copy items if needed” and “Create groups” before clicking Finish.

Familiarize yourself with the new views. They work together to display the hike data loaded into your model.

Step 5

In `HikeView`, experiment with showing and hiding the graph.

Be sure to use the Live preview throughout this tutorial so you can experiment with the results of each step.

Video with custom controls.

Play

Section 2

## Add animations to individual views

When you use the `animation(_:)` modifier on an equatable view, SwiftUI animates any changes to animatable properties of the view. A view’s color, opacity, rotation, size, and other properties are all animatable. When the view isn’t equatable, you can use the `animation(_:value:)` modifier to start animations when the specified value changes.

In `HikeView`, turn on animation for the button’s rotation by adding an animation modifier that begins on changes of the `showDetail` value.

HikeView.swift

import SwiftUI

struct HikeView: View {
var hike: Hike
@State private var showDetail = false

var body: some View {
VStack {
HStack {
HikeGraph(hike: hike, path: \.elevation)
.frame(width: 50, height: 30)

VStack(alignment: .leading) {
Text(hike.name)
.font(.headline)
Text(hike.distanceText)
}

Spacer()

Button {
showDetail.toggle()
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.padding()
.animation(.easeInOut, value: showDetail)
}
}

if showDetail {
HikeDetail(hike: hike)
}
}
}
}

.rotationEffect(.degrees(showDetail ? 90 : 0))
.padding()
.animation(.easeInOut, value: showDetail)
}
}

Preview

Add another animatable change by making the button larger when the graph is visible.

The animation modifier applies to all animatable changes within the views it wraps.

Button {
showDetail.toggle()
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.easeInOut, value: showDetail)
}
}

.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.easeInOut, value: showDetail)

Change the animation type from `easeInOut` to `spring()`.

SwiftUI includes basic animations with predefined or custom easing, as well as spring and fluid animations. You can adjust an animation’s speed, set a delay before an animation starts, or specify that an animation repeats.

Button {
showDetail.toggle()
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.spring(), value: showDetail)
}
}

.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.spring(), value: showDetail)
}
}

Try turning off animation for the rotation by adding another animation modifier just above the `scaleEffect` modifier.

Button {
showDetail.toggle()
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.animation(nil, value: showDetail)
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.spring(), value: showDetail)
}
}

.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.animation(nil, value: showDetail)
.scaleEffect(showDetail ? 1.5 : 1)
.padding()

Remove both animation modifiers before moving on to the next section.

Button {
showDetail.toggle()
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))

.scaleEffect(showDetail ? 1.5 : 1)
.padding()

}
}

.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))

Section 3

## Animate the effects of state changes

Now that you’ve learned how to apply animations to individual views, it’s time to add animations in places where you change your state’s value.

Here, you’ll apply animations to all of the changes that occur when a user taps a button and toggles the `showDetail` state property.

Wrap the call to `showDetail.toggle()` with a call to the `withAnimation` function.

Both of the views affected by the `showDetail` property — the disclosure button and the `HikeDetail` view — now have animated transitions.

Button {
withAnimation {
showDetail.toggle()
}
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
}
}

Button {
withAnimation {
showDetail.toggle()
}

Slow down the animation to see how SwiftUI animations are interruptible.

Pass a four-second long `basic` animation to the `withAnimation` function.

You can pass the same kinds of animations to the `withAnimation` function that you passed to the `animation(_:value:)` modifier.

Button {
withAnimation(.easeInOut(duration: 4)) {
showDetail.toggle()
}
} label: {
Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
}
}

Button {
withAnimation(.easeInOut(duration: 4)) {
showDetail.toggle()
}

Experiment with opening and closing the graph view mid-animation.

Before continuing to the next section, restore the `withAnimation` function to use the default animation by removing the call’s input parameter.

Section 4

## Customize view transitions

By default, views transition on- and offscreen by fading in and out. You can customize this transition by using the `transition(_:)` modifier.

Add a `transition(_:)` modifier to the conditionally visible `HikeView`.

Now the graph appears and disappears by sliding in and out of sight.

if showDetail {
HikeDetail(hike: hike)
.transition(.slide)
}
}
}
}

if showDetail {
HikeDetail(hike: hike)
.transition(.slide)
}
}

Extract the transition that you just added as a static property of `AnyTransition`, and access the new property in the view’s transition modifier.

This keeps your code clean as you expand the custom transition.

extension AnyTransition {
static var moveAndFade: AnyTransition {
AnyTransition.slide
}
}

if showDetail {
HikeDetail(hike: hike)
.transition(.moveAndFade)
}
}
}
}

struct HikeView: View {
var hike: Hike

Switch to using the `move(edge:)` transition, so that the graph slides in and out from the same side.

extension AnyTransition {
static var moveAndFade: AnyTransition {
AnyTransition.move(edge: .trailing)
}
}

Use the `asymmetric(insertion:removal:)` modifier to provide different transitions for when the view appears and disappears.

extension AnyTransition {
static var moveAndFade: AnyTransition {
.asymmetric(
insertion: .move(edge: .trailing).combined(with: .opacity),
removal: .scale.combined(with: .opacity)
)
}
}

Section 5

## Compose animations for complex effects

The graph switches between three different sets of data when you click the buttons below the bars. In this section, you’ll use a composed animation to give the capsules that make up the graph a dynamic, rippling transition.

In `HikeView`, change the default value for `showDetail` to `true`, and pin the preview to the canvas.

This makes it possible for you to see the graph in context while you work on the animation in another file.

In `HikeGraph`, define a new `ripple` animation and apply it to each generated graph capsule.

HikeGraph.swift

extension Animation {

Animation.default
}
}

struct HikeGraph: View {
var hike: Hike
var path: KeyPath<Hike.Observation, Range<Double>>

var color: Color {
switch path {
case \.elevation:
return .gray
case \.heartRate:
return Color(hue: 0, saturation: 0.5, brightness: 0.7)
case \.pace:
return Color(hue: 0.7, saturation: 0.4, brightness: 0.7)
default:
return .black
}
}

var body: some View {
let data = hike.observations
let overallRange = rangeOfRanges(data.lazy.map { $0[keyPath: path] })
let maxMagnitude = data.map { magnitude(of: $0[keyPath: path]) }.max()!
let heightRatio = 1 - CGFloat(maxMagnitude / magnitude(of: overallRange))

return GeometryReader { proxy in
HStack(alignment: .bottom, spacing: proxy.size.width / 120) {
ForEach(Array(data.enumerated()), id: \.offset) { index, observation in
GraphCapsule(
index: index,
color: color,
height: proxy.size.height,
range: observation[keyPath: path],
overallRange: overallRange
)
.animation(.ripple())
}
.offset(x: 0, y: proxy.size.height * heightRatio)
}
}
}
}

struct HikeGraph: View {
var hike: Hike

Switch the animation to a spring animation, with a reduced damping fraction to make the bars hop.

You can see the effect of the animation by switching between elevation, heart rate, and pace in the Live preview.

Animation.spring(dampingFraction: 0.5)
}
}

Speed up the animation a bit, to shorten the time each bar takes to move to its new position.

Animation.spring(dampingFraction: 0.5)
.speed(2)
}
}

Add a delay to each animation that’s based on the capsule’s position on the graph.

Animation.spring(dampingFraction: 0.5)
.speed(2)
.delay(0.03 * Double(index))
}
}

return GeometryReader { proxy in
HStack(alignment: .bottom, spacing: proxy.size.width / 120) {
ForEach(Array(data.enumerated()), id: \.offset) { index, observation in
GraphCapsule(
index: index,
color: color,
height: proxy.size.height,
range: observation[keyPath: path],
overallRange: overallRange
)
.animation(.ripple(index: index))
}
.offset(x: 0, y: proxy.size.height * heightRatio)
}
}
}
}

Animation.spring(dampingFraction: 0.5)
.speed(2)

Step 6

Observe how the custom animation provides a rippling effect when transitioning between graphs.

Be sure to unpin the preview before moving on to the next tutorial.

## Check Your Understanding

Question 1 of 3

How do you prevent the rotation effect from being animated in the following example?

Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.spring(), value: showDetail)

Possible answers

Pass `nil` to the `animation(_:value:)` modifier.

Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.rotationEffect(.degrees(showDetail ? 90 : 0))
.animation(nil, value: showDetail)
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.spring(), value: showDetail)

The `rotationEffect(_:)` modifier can’t be animated, so you don’t need to change the code to prevent animation.

Shield the rotation from being animated by applying the `withoutAnimation(_:)` modifier.

Label("Graph", systemImage: "chevron.right.circle")
.labelStyle(.iconOnly)
.imageScale(.large)
.withoutAnimation {
$0.rotationEffect(.degrees(showDetail ? 90 : 0))
}
.scaleEffect(showDetail ? 1.5 : 1)
.padding()
.animation(.spring(), value: showDetail)

Submit Next question

Next

## Composing complex interfaces

The category view for Landmarks shows a vertically scrolling list of horizontally scrolling landmarks. As you build this view and connect it to your existing views, you’ll explore how composed views can adapt to different device sizes and orientations.

Get started

---

# https://developer.apple.com/tutorials/swiftui/working-with-ui-controls

App design and layout

# Working with UI controls

In the Landmarks app, users can create a profile to express their personality. To give users the ability to change their profile, you’ll add an edit mode and design the preferences screen.

You’ll work with a variety of common user interface controls for data entry, and update the Landmarks model types whenever the user saves their changes.

Follow the steps to build this project, or download the finished project to explore on your own.

25

mins

Section 1

## Display a user profile

The Landmarks app locally stores some configuration details and preferences. Before the user edits their details, they’re displayed in a summary view that doesn’t have any editing controls.

Step 1

Start by defining a user profile in a new Swift file named `Profile.swift` that you add to your project’s Model group.

Profile.swift

import Foundation

struct Profile {
var username: String
var prefersNotifications = true
var seasonalPhoto = Season.winter
var goalDate = Date()

static let `default` = Profile(username: "g_kumar")

enum Season: String, CaseIterable, Identifiable {
case spring = "🌷"
case summer = "🌞"
case autumn = "🍂"
case winter = "☃️"

var id: String { rawValue }
}
}

No Preview

Step 2

Next, create a new group named Profiles under the Views group, and then add a view named `ProfileHost` to that group with a text view that displays the username of a stored profile.

The `ProfileHost` view will host both a static, summary view of profile information and an edit mode.

ProfileHost.swift

import SwiftUI

struct ProfileHost: View {
@State private var draftProfile = Profile.default

var body: some View {
Text("Profile for: \(draftProfile.username)")
}
}

#Preview {
ProfileHost()
}

#Preview {

Preview

Step 3

Create another view in the Profiles group named `ProfileSummary` that takes a `Profile` instance and displays some basic user information.

The profile summary takes a `Profile` value rather than a binding to the profile because the parent view, `ProfileHost`, manages the state for this view.

ProfileSummary.swift

struct ProfileSummary: View {
var profile: Profile

var body: some View {
ScrollView {
VStack(alignment: .leading, spacing: 10) {
Text(profile.username)
.bold()
.font(.title)

Text("Notifications: \(profile.prefersNotifications ? "On": "Off" )")
Text("Seasonal Photos: \(profile.seasonalPhoto.rawValue)")
Text("Goal Date: ") + Text(profile.goalDate, style: .date)
}
}
}
}

#Preview {
ProfileSummary(profile: Profile.default)
}

#Preview {

Step 4

Update `ProfileHost` to display the new summary view.

var body: some View {
VStack(alignment: .leading, spacing: 20) {
ProfileSummary(profile: draftProfile)
}
.padding()
}
}

#Preview {

Step 5

Create a new view named `HikeBadge` in the Hikes folder that composes the `Badge` from Drawing paths and shapes along with some descriptive text about the hike.

The badge is just a graphic, so the text in `HikeBadge` along with the `accessibilityLabel(_:)` modifier make the meaning of the badge clearer to other users.

HikeBadge.swift

struct HikeBadge: View {
var name: String

var body: some View {
VStack(alignment: .center) {
Badge()
.frame(width: 300, height: 300)
.scaleEffect(1.0 / 3.0)
.frame(width: 100, height: 100)
Text(name)
.font(.caption)
.accessibilityLabel("Badge for \(name).")
}
}
}

#Preview {
HikeBadge(name: "Preview Testing")
}

#Preview {

Step 6

Update `ProfileSummary` to add several badges with varying hues and reasons for earning the badge.

Text("Notifications: \(profile.prefersNotifications ? "On": "Off" )")
Text("Seasonal Photos: \(profile.seasonalPhoto.rawValue)")
Text("Goal Date: ") + Text(profile.goalDate, style: .date)

Divider()

VStack(alignment: .leading) {
Text("Completed Badges")
.font(.headline)

ScrollView(.horizontal) {
HStack {
HikeBadge(name: "First Hike")
HikeBadge(name: "Earth Day")
.hueRotation(Angle(degrees: 90))
HikeBadge(name: "Tenth Hike")
.grayscale(0.5)
.hueRotation(Angle(degrees: 45))
}
.padding(.bottom)
}
}
}
}
}
}

#Preview {

Text("Seasonal Photos: \(profile.seasonalPhoto.rawValue)")
Text("Goal Date: ") + Text(profile.goalDate, style: .date)

ScrollView(.horizontal) {
HStack {
HikeBadge(name: "First Hike")
HikeBadge(name: "Earth Day")
.hueRotation(Angle(degrees: 90))
HikeBadge(name: "Tenth Hike")
.grayscale(0.5)
.hueRotation(Angle(degrees: 45))
}
.padding(.bottom)
}
}
}
}

Step 7

Finish off the profile summary by including a `HikeView` from Animating views and transitions.

To use the hike data, you also need to add a model data environment property.

struct ProfileSummary: View {
@Environment(ModelData.self) var modelData
var profile: Profile

ScrollView(.horizontal) {
HStack {
HikeBadge(name: "First Hike")
HikeBadge(name: "Earth Day")
.hueRotation(Angle(degrees: 90))
HikeBadge(name: "Tenth Hike")
.grayscale(0.5)
.hueRotation(Angle(degrees: 45))
}
.padding(.bottom)
}
}

VStack(alignment: .leading) {
Text("Recent Hikes")
.font(.headline)

HikeView(hike: modelData.hikes[0])
}
}
}
}
}

#Preview {
ProfileSummary(profile: Profile.default)
.environment(ModelData())
}

Step 8

In `CategoryHome`, add a user profile button to the navigation bar using the `toolbar` modifier, and present the `ProfileHost` view when the user taps it.

CategoryHome.swift

struct CategoryHome: View {
@Environment(ModelData.self) var modelData
@State private var showingProfile = false

var body: some View {
NavigationSplitView {
List {
modelData.features[0].image
.resizable()
.scaledToFill()
.frame(height: 200)
.clipped()
.listRowInsets(EdgeInsets())

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
.listRowInsets(EdgeInsets())
}
.navigationTitle("Featured")
.toolbar {
Button {
showingProfile.toggle()
} label: {
Label("User Profile", systemImage: "person.crop.circle")
}
}
.sheet(isPresented: $showingProfile) {
ProfileHost()
.environment(modelData)
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {
CategoryHome()
.environment(ModelData())
}

var body: some View {

Step 9

Add the `listStyle` modifier to pick a list style that better suits the content.

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
.listRowInsets(EdgeInsets())
}
.listStyle(.inset)
.navigationTitle("Featured")
.toolbar {
Button {
showingProfile.toggle()
} label: {
Label("User Profile", systemImage: "person.crop.circle")
}
}
.sheet(isPresented: $showingProfile) {
ProfileHost()
.environment(modelData)
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

.listRowInsets(EdgeInsets())
}
.listStyle(.inset)
.navigationTitle("Featured")
.toolbar {

Step 10

Make sure you are on Live preview and try tapping the profile button to examine the profile summary.

Video with custom controls.

Content description: A screenshot of the preview in Xcode, showing the preferences screen as it would appear on iPhone.

Play

Section 2

## Add an edit mode

Users need to toggle between viewing or editing their profile details. You’ll add an edit mode by adding an `EditButton` to the existing `ProfileHost`, and then creating a view with controls for editing individual values.

Select `ProfileHost` and add the model data as an environment property to the preview.

Even though this view doesn’t use a property with the `@Environment` property wrapper, `ProfileSummary`, a child of this view, does. So without the modifier, the preview fails.

#Preview {
ProfileHost()
.environment(ModelData())
}

#Preview {

Add an `Environment` view property that keys off of the environment’s `\.editMode`.

SwiftUI provides storage in the environment for values you can access using the `@Environment` property wrapper. Earlier you used `@Environment` to retrieve a class that you stored in the environment. Here, you use it to access the `editMode` value that’s built into the environment to read or write the edit scope.

struct ProfileHost: View {
@Environment(\.editMode) var editMode
@State private var draftProfile = Profile.default

#Preview {

Create an Edit button that toggles the environment’s `editMode` value on and off.

The `EditButton` controls the same `editMode` environment value that you accessed in the previous step.

var body: some View {
VStack(alignment: .leading, spacing: 20) {
HStack {
Spacer()
EditButton()
}

ProfileSummary(profile: draftProfile)
}
.padding()
}
}

#Preview {

ProfileSummary(profile: draftProfile)
}

Update the `ModelData` class to include an instance of the user profile that persists even after the user dismisses the profile view.

ModelData.swift

@Observable
class ModelData {
var landmarks: [Landmark] = load("landmarkData.json")
var hikes: [Hike] = load("hikeData.json")
var profile = Profile.default

var features: [Landmark] {
landmarks.filter { $0.isFeatured }
}

var categories: [String: [Landmark]] {
Dictionary(
grouping: landmarks,
by: { $0.category.rawValue }
)
}
}

let data: Data

guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
else {
fatalError("Couldn't find \(filename) in main bundle.")
}

do {
data = try Data(contentsOf: file)
} catch {
fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
}

do {
let decoder = JSONDecoder()
return try decoder.decode(T.self, from: data)
} catch {
fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
}
}

var landmarks: [Landmark] = load("landmarkData.json")
var hikes: [Hike] = load("hikeData.json")
var profile = Profile.default

var features: [Landmark] {

Read the user’s profile data from the environment to pass control of the data to the profile host.

To avoid updating the global app state before confirming any edits — such as while the user enters their name — the editing view operates on a copy of itself.

struct ProfileHost: View {
@Environment(\.editMode) var editMode
@Environment(ModelData.self) var modelData
@State private var draftProfile = Profile.default

ProfileSummary(profile: modelData.profile)
}
.padding()
}
}

#Preview {

Add a conditional view that displays either the static profile or the view for Edit mode.

You can see the effect of entering edit mode by running the Live preview and tapping the edit button. For now, the Edit mode view is just a static text field.

if editMode?.wrappedValue == .inactive {
ProfileSummary(profile: modelData.profile)
} else {
Text("Profile Editor")
}
}
.padding()
}
}

#Preview {

}

if editMode?.wrappedValue == .inactive {
ProfileSummary(profile: modelData.profile)
} else {
Text("Profile Editor")
}
}
.padding()

#Preview {

Section 3

## Define the profile editor

The user profile editor consists primarily of different controls that change individual details in the profile. Some items in the profile, like the badges, aren’t user-editable, so they don’t appear in the editor.

For consistency with the profile summary, you’ll add the profile details in the same order in the editor.

Create a new view named `ProfileEditor` and include a binding to the draft copy of the user’s profile.

The first control in the view is a `TextField`, which controls and updates a string binding — in this case, the user’s chosen display name. You provide a label and a binding to a string when creating a text field.

ProfileEditor.swift

struct ProfileEditor: View {
@Binding var profile: Profile

var body: some View {
List {
HStack {
Text("Username")
Spacer()
TextField("Username", text: $profile.username)
.foregroundStyle(.secondary)
.multilineTextAlignment(.trailing)
}
}
}
}

#Preview {
ProfileEditor(profile: .constant(.default))
}

#Preview {

Update the conditional content in `ProfileHost` to include the profile editor and pass along the profile binding.

Now the edit profile view displays when you tap **Edit**.

if editMode?.wrappedValue == .inactive {
ProfileSummary(profile: modelData.profile)
} else {
ProfileEditor(profile: $draftProfile)
}
}
.padding()
}
}

#Preview {

ProfileSummary(profile: modelData.profile)
} else {
ProfileEditor(profile: $draftProfile)
}
}

Add a toggle that corresponds with the user’s preference for receiving notifications about landmark-related events.

Toggles are controls that are either on or off, so they’re a good fit for Boolean values like a yes or no preference.

var body: some View {
List {
HStack {
Text("Username")
Spacer()
TextField("Username", text: $profile.username)
.foregroundStyle(.secondary)
.multilineTextAlignment(.trailing)
}

Toggle(isOn: $profile.prefersNotifications) {
Text("Enable Notifications")
}
}
}
}

#Preview {

.multilineTextAlignment(.trailing)
}

Toggle(isOn: $profile.prefersNotifications) {
Text("Enable Notifications")
}
}
}

Place a `Picker` control and its label in the `HStack` to make the landmark photos have a selectable preferred season.

Toggle(isOn: $profile.prefersNotifications) {
Text("Enable Notifications")
}

Picker("Seasonal Photo", selection: $profile.seasonalPhoto) {
ForEach(Profile.Season.allCases) { season in
Text(season.rawValue).tag(season)
}
}
}
}
}

#Preview {

Text("Enable Notifications")
}

Picker("Seasonal Photo", selection: $profile.seasonalPhoto) {
ForEach(Profile.Season.allCases) { season in
Text(season.rawValue).tag(season)
}
}
}
}

Finally, add a `DatePicker` below the season selector to make the landmark visitation goal date modifiable.

let min = Calendar.current.date(byAdding: .year, value: -1, to: profile.goalDate)!
let max = Calendar.current.date(byAdding: .year, value: 1, to: profile.goalDate)!
return min...max
}

Picker("Seasonal Photo", selection: $profile.seasonalPhoto) {
ForEach(Profile.Season.allCases) { season in
Text(season.rawValue).tag(season)
}
}

DatePicker(selection: $profile.goalDate, in: dateRange, displayedComponents: .date) {
Text("Goal Date")
}
}
}
}

#Preview {

@Binding var profile: Profile

var body: some View {
List {

#Preview {

Section 4

## Delay edit propagation

To make it so edits don’t take effect until after the user exits edit mode, you use the draft copy of their profile during editing, then assign the draft copy to the real copy only when the user confirms an edit.

Add a cancel button to `ProfileHost`.

Unlike the `Done` button that `EditButton` provides, the `Cancel` button doesn’t apply the edits to the real profile data in its closure.

var body: some View {
VStack(alignment: .leading, spacing: 20) {
HStack {
if editMode?.wrappedValue == .active {
Button("Cancel", role: .cancel) {
draftProfile = modelData.profile
editMode?.animation().wrappedValue = .inactive
}
}
Spacer()
EditButton()
}

#Preview {

VStack(alignment: .leading, spacing: 20) {
HStack {
if editMode?.wrappedValue == .active {
Button("Cancel", role: .cancel) {
draftProfile = modelData.profile
editMode?.animation().wrappedValue = .inactive
}
}
Spacer()
EditButton()

Apply the `onAppear(perform:)` and `onDisappear(perform:)` modifiers to populate the editor with the correct profile data and update the persistent profile when the user taps the Done button.

Otherwise, the old values appear the next time edit mode activates.

if editMode?.wrappedValue == .inactive {
ProfileSummary(profile: modelData.profile)
} else {
ProfileEditor(profile: $draftProfile)
.onAppear {
draftProfile = modelData.profile
}
.onDisappear {
modelData.profile = draftProfile
}
}
}
.padding()
}
}

#Preview {

} else {
ProfileEditor(profile: $draftProfile)
.onAppear {
draftProfile = modelData.profile
}
.onDisappear {
modelData.profile = draftProfile
}
}
}

#Preview {

## Check Your Understanding

Question 1 of 3

How do you update a view when the editing state changes; for example, when a user taps Done after editing their profile?

Possible answers

struct EditableNameView: View {
@State var isEditing = false
@State var name = ""
var body: some View {
TextField("Name", text: $name)
.disabled(!isEditing)
}
}
struct EditableNameView: View {
@Environment(\.editMode) var mode
@State var name = ""
var body: some View {
TextField("Name", text: $name)
.disabled(mode?.wrappedValue == .inactive)
}
}
struct EditableNameView: View {
@State var name = ""
var body: some View {
TextField("Name", text: $name)
.onEditingChanged { isEditing in
$0.disabled = !isEditing
}
}
}

Submit Next question

Next

## Interfacing with UIKit

SwiftUI works seamlessly with the existing UI frameworks on all Apple platforms. For example, you can place UIKit views and view controllers inside SwiftUI views, and vice versa.

Get started

---

# https://developer.apple.com/tutorials/swiftui/interfacing-with-uikit

Framework integration

# Interfacing with UIKit

SwiftUI works seamlessly with the existing UI frameworks on all Apple platforms. For example, you can place UIKit views and view controllers inside SwiftUI views, and vice versa.

This tutorial shows you how to convert the featured landmark from the home screen to wrap instances of `UIPageViewController` and `UIPageControl`. You’ll use `UIPageViewController` to display a carousel of SwiftUI views, and use state variables and bindings to coordinate data updates throughout the user interface.

Follow the steps to build this project, or download the finished project to explore on your own.

25

mins

Section 1

## Create a view to represent a UIPageViewController

To represent UIKit views and view controllers in SwiftUI, you create types that conform to the `UIViewRepresentable` and `UIViewControllerRepresentable` protocols. Your custom types create and configure the UIKit types that they represent, while SwiftUI manages their life cycle and updates them when needed.

Step 1

Create a PageView group in your project’s Views folder, and add a new Swift file named `PageViewController.swift`; Declare the `PageViewController` type as conforming to `UIViewControllerRepresentable.`

The page view controller stores an array of `Page` instances, which must be a type of `View`. These are the pages you use to scroll between landmarks.

PageViewController.swift

import SwiftUI
import UIKit

var pages: [Page]

}

No Preview

Next, add the two requirements for the `UIViewControllerRepresentable` protocol.

Step 2

Add a `makeUIViewController(context:)` method that creates a `UIPageViewController` with the desired configuration.

SwiftUI calls this method a single time when it’s ready to display the view, and then manages the view controller’s life cycle.

let pageViewController = UIPageViewController(
transitionStyle: .scroll,
navigationOrientation: .horizontal)

return pageViewController
}
}

Step 3

Add an `updateUIViewController(_:context:)` method that calls `setViewControllers(_:direction:animated:)` to provide a view controller for display.

For now, you create the `UIHostingController` that hosts the `page` SwiftUI view on every update. Later, you’ll make this more efficient by initializing the controller only once for the life of the page view controller.

return pageViewController
}

func updateUIViewController(_ pageViewController: UIPageViewController, context: Context) {
pageViewController.setViewControllers(
[UIHostingController(rootView: pages[0])], direction: .forward, animated: true)
}
}

Before you continue, prepare a feature card for use as a page.

Step 4

Drag the images in the downloaded project files’ Resources directory into your app’s Asset catalog.

A landmark’s feature image, if it exists, has different dimensions than the regular image.

Step 5

Add a computed property to the `Landmark` structure that returns the feature image, if it exists.

Landmark.swift

import Foundation
import SwiftUI
import CoreLocation

struct Landmark: Hashable, Codable, Identifiable {
var id: Int
var name: String
var park: String
var state: String
var description: String
var isFavorite: Bool
var isFeatured: Bool

var category: Category
enum Category: String, CaseIterable, Codable, Hashable {
case lakes = "Lakes"
case rivers = "Rivers"
case mountains = "Mountains"
}

private var imageName: String
var image: Image {
Image(imageName)
}
var featureImage: Image? {
isFeatured ? Image(imageName + "_feature") : nil
}

private var coordinates: Coordinates
var locationCoordinate: CLLocationCoordinate2D {
CLLocationCoordinate2D(
latitude: coordinates.latitude,
longitude: coordinates.longitude)
}

struct Coordinates: Hashable, Codable {
var latitude: Double
var longitude: Double
}
}

Image(imageName)
}
var featureImage: Image? {
isFeatured ? Image(imageName + "_feature") : nil
}

private var coordinates: Coordinates

Step 6

Add a new SwiftUI view file, named `FeatureCard.swift` that displays the landmark’s feature image.

Include the aspect ratio modifier so it mimics the aspect ratio of the view where `FeatureCard` will eventually preview later.

FeatureCard.swift

import SwiftUI

struct FeatureCard: View {
var landmark: Landmark

var body: some View {
landmark.featureImage?
.resizable()
}
}

#Preview {
FeatureCard(landmark: ModelData().features[0])
.aspectRatio(3 / 2, contentMode: .fit)
}

#Preview {

Preview

Step 7

Overlay text information about the landmark on the image.

var body: some View {
landmark.featureImage?
.resizable()
.overlay {
TextOverlay(landmark: landmark)
}
}
}

struct TextOverlay: View {
var landmark: Landmark

var gradient: LinearGradient {
.linearGradient(
Gradient(colors: [.black.opacity(0.6), .black.opacity(0)]),
startPoint: .bottom,
endPoint: .center)
}

var body: some View {
ZStack(alignment: .bottomLeading) {
gradient
VStack(alignment: .leading) {
Text(landmark.name)
.font(.title)
.bold()
Text(landmark.park)
}
.padding()
}
.foregroundStyle(.white)
}
}

#Preview {

landmark.featureImage?
.resizable()
.overlay {
TextOverlay(landmark: landmark)
}
}
}

Next, you’ll create a custom view to present your `UIViewControllerRepresentable` view.

Step 8

Create a new SwiftUI view file, named `PageView.swift`, and update the `PageView` type to declare `PageViewController` as a child view.

The preview fails because Xcode can’t infer a type for `Page`.

PageView.swift

var body: some View {
PageViewController(pages: pages)
}
}

#Preview {
PageView()
}

var body: some View {
PageViewController(pages: pages)

Step 9

Add the aspect ratio modifier and update the preview to pass the required array of views, and the preview starts working.

var body: some View {
PageViewController(pages: pages)
.aspectRatio(3 / 2, contentMode: .fit)
}
}

#Preview {
PageView(pages: ModelData().features.map { FeatureCard(landmark: $0) })
}

Section 2

## Create the view controller’s data source

In a few short steps, you’ve done a lot — the `PageViewController` uses a `UIPageViewController` to show content from a SwiftUI view. Now it’s time to enable swiping interactions to move from page to page.

A SwiftUI view that represents a UIKit view controller can define a `Coordinator` type that SwiftUI manages and provides as part of the representable view’s context.

Declare a nested `Coordinator` class inside `PageViewController`.

SwiftUI manages your `UIViewControllerRepresentable` type’s coordinator, and provides it as part of the context when calling the methods you created above.

func updateUIViewController(_ pageViewController: UIPageViewController, context: Context) {
pageViewController.setViewControllers(
[UIHostingController(rootView: pages[0])], direction: .forward, animated: true)
}

class Coordinator: NSObject {
var parent: PageViewController

init(_ pageViewController: PageViewController) {
parent = pageViewController
}
}
}

[UIHostingController(rootView: pages[0])], direction: .forward, animated: true)
}

Add another method to `PageViewController` to make the coordinator.

SwiftUI calls this `makeCoordinator()` method before `makeUIViewController(context:)`, so that you have access to the coordinator object when configuring your view controller.

Coordinator(self)
}

let pageViewController = UIPageViewController(

Initialize an array of controllers in the coordinator using the `pages` array of views.

The coordinator is a good place to store these controllers, because the system initializes them only once, and before you need them to update the view controller.

func updateUIViewController(_ pageViewController: UIPageViewController, context: Context) {
pageViewController.setViewControllers(
[context.coordinator.controllers[0]], direction: .forward, animated: true)
}

class Coordinator: NSObject {
var parent: PageViewController
var controllers = UIViewController

init(_ pageViewController: PageViewController) {
parent = pageViewController
controllers = parent.pages.map { UIHostingController(rootView: $0) }
}
}
}

Add `UIPageViewControllerDataSource` conformance to the `Coordinator` type, and implement the two required methods.

These two methods establish the relationships between view controllers, so that you can swipe back and forth between them.

class Coordinator: NSObject, UIPageViewControllerDataSource {
var parent: PageViewController
var controllers = UIViewController

init(_ pageViewController: PageViewController) {
parent = pageViewController
controllers = parent.pages.map { UIHostingController(rootView: $0) }
}

func pageViewController(
_ pageViewController: UIPageViewController,

{
guard let index = controllers.firstIndex(of: viewController) else {
return nil
}
if index == 0 {
return controllers.last
}
return controllers[index - 1]
}

{
guard let index = controllers.firstIndex(of: viewController) else {
return nil
}
if index + 1 == controllers.count {
return controllers.first
}
return controllers[index + 1]
}
}
}

Add the coordinator as the data source of the `UIPageViewController`.

let pageViewController = UIPageViewController(
transitionStyle: .scroll,
navigationOrientation: .horizontal)
pageViewController.dataSource = context.coordinator

transitionStyle: .scroll,
navigationOrientation: .horizontal)
pageViewController.dataSource = context.coordinator

return pageViewController

Section 3

## Track the page in a SwiftUI view’s state

To prepare for adding a custom `UIPageControl`, you need a way to track the current page from within `PageView`.

To do this, you’ll declare a `@State` property in `PageView`, and pass a binding to this property down to the `PageViewController` view. The `PageViewController` updates the binding to match the visible page.

Start by adding a `currentPage` binding as a property of `PageViewController`.

In addition to declaring the `@Binding` property, you also update the call to `setViewControllers(_:direction:animated:)`, passing the value of the `currentPage` binding.

var pages: [Page]
@Binding var currentPage: Int

func updateUIViewController(_ pageViewController: UIPageViewController, context: Context) {
pageViewController.setViewControllers(
[context.coordinator.controllers[currentPage]], direction: .forward, animated: true)
}

Declare the `@State` variable in `PageView`, and pass a binding to the property when creating the child `PageViewController`.

var pages: [Page]
@State private var currentPage = 0

var body: some View {
PageViewController(pages: pages, currentPage: $currentPage)
.aspectRatio(3 / 2, contentMode: .fit)
}
}

#Preview {

var body: some View {

Test that the value flows through the binding to the `PageViewController` by changing its initial value.

var pages: [Page]
@State private var currentPage = 1

#Preview {

Add a text view with the `currentPage` property, so that you can keep an eye on the `@State` property’s value.

Observe that when you swipe from page to page, the value doesn’t change.

var body: some View {
VStack {
PageViewController(pages: pages, currentPage: $currentPage)
Text("Current Page: \(currentPage)")
}
.aspectRatio(3 / 2, contentMode: .fit)
}
}

#Preview {

In `PageViewController.swift`, conform the coordinator to `UIPageViewControllerDelegate`, and add the `pageViewController(_:didFinishAnimating:previousViewControllers:transitionCompleted completed: Bool)` method.

Because SwiftUI calls this method whenever a page switching animation completes, you can find the index of the current view controller and update the binding.

class Coordinator: NSObject, UIPageViewControllerDataSource, UIPageViewControllerDelegate {
var parent: PageViewController
var controllers = UIViewController

{
guard let index = controllers.firstIndex(of: viewController) else {
return nil
}
if index + 1 == controllers.count {
return controllers.first
}
return controllers[index + 1]
}

func pageViewController(
_ pageViewController: UIPageViewController,
didFinishAnimating finished: Bool,
previousViewControllers: [UIViewController],
transitionCompleted completed: Bool) {
if completed,
let visibleViewController = pageViewController.viewControllers?.first,
let index = controllers.firstIndex(of: visibleViewController) {
parent.currentPage = index
}
}
}
}

Assign the coordinator as the delegate for the `UIPageViewController`, in addition to the data source.

With the binding connected in both directions, the text view updates to show the correct page number after each swipe.

let pageViewController = UIPageViewController(
transitionStyle: .scroll,
navigationOrientation: .horizontal)
pageViewController.dataSource = context.coordinator
pageViewController.delegate = context.coordinator

navigationOrientation: .horizontal)
pageViewController.dataSource = context.coordinator
pageViewController.delegate = context.coordinator

Section 4

## Add a custom page control

You’re ready to add a custom `UIPageControl` to your view, wrapped in SwiftUI `UIViewRepresentable` view.

Create a new SwiftUI view file, named `PageControl.swift`. Update the `PageControl` type to conform to the `UIViewRepresentable` protocol.

`UIViewRepresentable` and `UIViewControllerRepresentable` types have the same life cycle, with methods that correspond to their underlying UIKit types.

PageControl.swift

struct PageControl: UIViewRepresentable {
var numberOfPages: Int
@Binding var currentPage: Int

let control = UIPageControl()
control.numberOfPages = numberOfPages

return control
}

func updateUIView(_ uiView: UIPageControl, context: Context) {
uiView.currentPage = currentPage
}
}

Replace the text box with the page control, switching from a `VStack` to a `ZStack` for layout.

Because you’re passing the page count and the binding to the current page, the page control is already showing the correct values.

var body: some View {
ZStack(alignment: .bottomTrailing) {
PageViewController(pages: pages, currentPage: $currentPage)
PageControl(numberOfPages: pages.count, currentPage: $currentPage)
.frame(width: CGFloat(pages.count * 18))
.padding(.trailing)
}
.aspectRatio(3 / 2, contentMode: .fit)
}
}

#Preview {

var body: some View {
ZStack(alignment: .bottomTrailing) {
PageViewController(pages: pages, currentPage: $currentPage)
PageControl(numberOfPages: pages.count, currentPage: $currentPage)

Next, make the page control interactive so users can tap one side or the other to move between pages.

Create a nested `Coordinator` type in `PageControl`, and add a `makeCoordinator()` method to create and return a new coordinator.

Because `UIControl` subclasses like `UIPageControl` use the target-action pattern instead of delegation, this `Coordinator` implements an `@objc` method to update the current page binding.

func updateUIView(_ uiView: UIPageControl, context: Context) {
uiView.currentPage = currentPage
}

class Coordinator: NSObject {
var control: PageControl

init(_ control: PageControl) {
self.control = control
}

@objc
func updateCurrentPage(sender: UIPageControl) {
control.currentPage = sender.currentPage
}
}
}

@Binding var currentPage: Int

let control = UIPageControl()

Add the coordinator as the target for the `valueChanged` event, specifying the `updateCurrentPage(sender:)` method as the action to perform.

let control = UIPageControl()
control.numberOfPages = numberOfPages
control.addTarget(
context.coordinator,
action: #selector(Coordinator.updateCurrentPage(sender:)),
for: .valueChanged)

return control

Finally, in `CategoryHome`, replace the placeholder feature image with the new page view.

CategoryHome.swift

struct CategoryHome: View {
@Environment(ModelData.self) var modelData
@State private var showingProfile = false

var body: some View {
NavigationSplitView {
List {
PageView(pages: modelData.features.map { FeatureCard(landmark: $0) })
.listRowInsets(EdgeInsets())

ForEach(modelData.categories.keys.sorted(), id: \.self) { key in
CategoryRow(categoryName: key, items: modelData.categories[key]!)
}
.listRowInsets(EdgeInsets())
}
.listStyle(.inset)
.navigationTitle("Featured")
.toolbar {
Button {
showingProfile.toggle()
} label: {
Label("User Profile", systemImage: "person.crop.circle")
}
}
.sheet(isPresented: $showingProfile) {
ProfileHost()
.environment(modelData)
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {
CategoryHome()
.environment(ModelData())
}

NavigationSplitView {
List {
PageView(pages: modelData.features.map { FeatureCard(landmark: $0) })
.listRowInsets(EdgeInsets())

Now try out all the different interactions — `PageView` shows how UIKit and SwiftUI views and controllers can work together.

Video with custom controls.

Content description: An animation that shows how users can swipe left and right between landmarks.

Play

## Check Your Understanding

Question 1 of 2

Which protocol do you use to bridge UIKit view controllers into SwiftUI?

Possible answers

`UIViewRepresentable`

`UIHostingController`

`UIViewControllerRepresentable`

Submit Next question

Next

## Creating a watchOS app

This tutorial gives you a chance to apply much of what you’ve already learned about SwiftUI, and — with little effort — migrate the Landmarks app to watchOS.

Get started

---

# https://developer.apple.com/tutorials/swiftui/building-lists-and-navigation

SwiftUI essentials

# Building lists and navigation

With the basic landmark detail view set up, you need to provide a way for users to see the full list of landmarks, and to view the details about each location.

You’ll create views that can show information about any landmark, and dynamically generate a scrolling list that a user can tap to see a detail view for a landmark. To fine-tune the UI, you’ll use Xcode to render previews at different device sizes.

Download the project files to begin building this project, and follow the steps below.

35

mins

Section 1

## Create a landmark model

In the first tutorial, you hard-coded information into all of your custom views. Here, you’ll create a model to store data that you can pass into your views.

Use the completed project from the previous tutorial and the resources available from this tutorial’s project files to get started.

Step 1

Drag `landmarkData.json` in the downloaded files’ Resources folder into your project’s navigation pane; in the dialog that appears, select “Copy items if needed” and the Landmarks target, and then click Finish.

You’ll use this sample data throughout the remainder of this tutorial, and for all that follow.

Step 2

Step 3

Define a `Landmark` structure with a few properties matching names of some of the keys in the `landmarkData` data file.

Adding `Codable` conformance makes it easier to move data between the structure and a data file. You’ll rely on the `Decodable` component of the `Codable` protocol later in this section to read data from file.

Landmark.swift

import Foundation

struct Landmark: Hashable, Codable {
var id: Int
var name: String
var park: String
var state: String
var description: String
}

No Preview

In the next few steps you’ll model the image associated with each landmark.

Step 4

Drag the JPG files from the project files’ Resources folder into your project’s asset catalog. Xcode creates a new image set for each image.

The new images join the one for Turtle Rock that you added in the previous tutorial.

Step 5

Add an `imageName` property to read the name of the image from the data, and a computed `image` property that loads an image from the asset catalog.

You make the property private because users of the `Landmarks` structure care only about the image itself.

import Foundation
import SwiftUI

struct Landmark: Hashable, Codable {
var id: Int
var name: String
var park: String
var state: String
var description: String

private var imageName: String
var image: Image {
Image(imageName)
}
}

struct Landmark: Hashable, Codable {

Next, you’ll manage information about the landmark’s location.

Step 6

Add a `coordinates` property to the structure using a nested `Coordinates` type that reflects the storage in the JSON data structure.

You mark this property as private because you’ll use it only to create a public computed property in the next step.

private var imageName: String
var image: Image {
Image(imageName)
}

private var coordinates: Coordinates

struct Coordinates: Hashable, Codable {
var latitude: Double
var longitude: Double
}
}

Image(imageName)
}

Step 7

Compute a `locationCoordinate` property that’s useful for interacting with the MapKit framework.

import Foundation
import SwiftUI
import CoreLocation

private var coordinates: Coordinates
var locationCoordinate: CLLocationCoordinate2D {
CLLocationCoordinate2D(
latitude: coordinates.latitude,
longitude: coordinates.longitude)
}

Finally, you’ll create an array initialized with landmarks from a file.

Step 8

Create a new Swift file in your project and name it `ModelData.swift`.

Step 9

Create a `load(_:)` method that fetches JSON data with a given name from the app’s main bundle.

The load method relies on the return type’s conformance to the `Decodable` protocol, which is one component of the `Codable` protocol.

ModelData.swift

let data: Data

guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
else {
fatalError("Couldn't find \(filename) in main bundle.")
}

do {
data = try Data(contentsOf: file)
} catch {
fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
}

do {
let decoder = JSONDecoder()
return try decoder.decode(T.self, from: data)
} catch {
fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
}
}

Step 10

Create an array of landmarks that you initialize from `landmarkData.json`.

var landmarks: [Landmark] = load("landmarkData.json")

Before moving on, group related files together to make it easier to manage your growing project.

Step 11

Put `ContentView`, `CircleImage`, and `MapView` into a Views group, `landmarkData` in a Resources group, and `Landmark` and `ModelData` into a Model group.

Section 2

## Create the row view

The first view you’ll build in this tutorial is a row for displaying details about each landmark. This row view stores information in a property for the landmark it displays, so that one view can display any landmark. Later, you’ll combine multiple rows into a list of landmarks.

Create a new SwiftUI view in the Views group named `LandmarkRow.swift`.

Add `landmark` as a stored property of `LandmarkRow`.

When you add the `landmark` property, the preview in the canvas stops working because the `LandmarkRow` type needs a landmark instance during initialization.

LandmarkRow.swift

import SwiftUI

struct LandmarkRow: View {
var landmark: Landmark

var body: some View {
Text("Hello, World!")
}
}

#Preview {
LandmarkRow()
}

var body: some View {
Text("Hello, World!")

To fix the preview, you’ll need to modify the preview’s view instantiation.

Inside the preview macro, add the landmark parameter to the `LandmarkRow` initializer, specifying the first element of the `landmarks` array.

The preview displays the text, “Hello, World!”.

#Preview {
LandmarkRow(landmark: landmarks[0])
}

#Preview {

Preview

With that fixed, you can build the layout for the row.

Embed the existing text view in an `HStack`.

var body: some View {
HStack {
Text("Hello, World!")
}
}
}

#Preview {

Modify the text view to use the `landmark` property’s `name`.

var body: some View {
HStack {
Text(landmark.name)
}
}
}

#Preview {

var body: some View {
HStack {
Text(landmark.name)
}
}

Complete the row by adding an image before the text view, and a spacer after it.

var body: some View {
HStack {
landmark.image
.resizable()
.frame(width: 50, height: 50)
Text(landmark.name)

Spacer()
}
}
}

#Preview {

Section 3

## Customize the row preview

Xcode automatically recognizes any previews that you declare with a preview macro in a view’s source file.

The canvas displays only one preview at a time, but you can define multiple previews and choose among them in the canvas. Alternatively, you can group views together to create a single preview of more than one version of a view.

Add a second preview macro that uses the the second element in the `landmarks` array.

Adding previews enables you to see how your views behave with different data.

#Preview {

#Preview {
LandmarkRow(landmark: landmarks[1])
}

#Preview {

Use the controls in the canvas to choose the second preview.

By default, the canvas labels previews using the line number they appear on.

The preview macro takes an optional `name` parameter that you can use to label a preview.

Give each preview a name to help distinguish between them.

#Preview("Turtle Rock") {

#Preview("Salmon") {

}

#Preview("Turtle Rock") {

Navigate between the two previews with the new labels. Try changing the selected preview again.

When you want to preview different versions of a view side by side, you can instead group them together in a single collection view.

Remove the second preview, and instead wrap the two versions of the row in a `Group`.

`Group` is a container for grouping view content. Xcode renders the group’s child views stacked as one preview in the canvas.

#Preview {
Group {
LandmarkRow(landmark: landmarks[0])
LandmarkRow(landmark: landmarks[1])
}
}

#Preview {

The code you write in the preview only changes what Xcode displays in the canvas.

#Preview {

#Preview {

Section 4

## Create the list of landmarks

When you use SwiftUI’s `List` type, you can display a platform-specific list of views. The elements of the list can be static, like the child views of the stacks you’ve created so far, or dynamically generated. You can even mix static and dynamically generated views.

Create a new SwiftUI view in the Views group named `LandmarkList.swift`.

Replace the default `Text` view with a `List`, and provide `LandmarkRow` instances with the first two landmarks as the list’s children.

The preview shows the two landmarks rendered in a list style that’s appropriate for iOS.

LandmarkList.swift

struct LandmarkList: View {
var body: some View {
List {
LandmarkRow(landmark: landmarks[0])
LandmarkRow(landmark: landmarks[1])
}
}
}

#Preview {
LandmarkList()
}

Section 5

## Make the list dynamic

Instead of specifying a list’s elements individually, you can generate rows directly from a collection.

You can create a list that displays the elements of a collection by passing your collection of data and a closure that provides a view for each element in the collection. The list transforms each element in the collection into a child view by using the supplied closure.

Remove the two static landmark rows, and instead pass the model data’s `landmarks` array to the `List` initializer.

Lists work with _identifiable_ data. You can make your data identifiable in one of two ways: by passing along with your data a key path to a property that uniquely identifies each element, or by making your data type conform to the `Identifiable` protocol.

struct LandmarkList: View {
var body: some View {
List(landmarks, id: \.id) { landmark in

}
}
}

#Preview {

}
}

Complete the dynamically-generated list by returning a `LandmarkRow` from the closure.

This creates one `LandmarkRow` for each element in the `landmarks` array.

struct LandmarkList: View {
var body: some View {
List(landmarks, id: \.id) { landmark in
LandmarkRow(landmark: landmark)
}
}
}

#Preview {

var body: some View {
List(landmarks, id: \.id) { landmark in
LandmarkRow(landmark: landmark)
}
}

Next, you’ll simplify the `List` code by adding `Identifiable` conformance to the `Landmark` type.

Switch to `Landmark.swift` and declare conformance to the `Identifiable` protocol.

The `Landmark` data already has the `id` property required by `Identifiable` protocol; you only need to add a property to decode it when reading the data.

struct Landmark: Hashable, Codable, Identifiable {
var id: Int
var name: String
var park: String
var state: String
var description: String

import CoreLocation

struct Landmark: Hashable, Codable, Identifiable {
var id: Int
var name: String

Switch

struct LandmarkList: View {
var body: some View {
List(landmarks) { landmark in
LandmarkRow(landmark: landmark)
}

#Preview {

Section 6

## Set up navigation between list and detail

The list renders properly, but you can’t tap an individual landmark to see that landmark’s detail page yet.

You add navigation capabilities to a list by embedding it in a `NavigationSplitView`, and then nesting each row in a `NavigationLink` to set up a transtition to a destination view.

Prepare a detail view using the content you created in the previous tutorial and update the main content view to display the list view instead.

Create a new SwiftUI view named `LandmarkDetail.swift`.

LandmarkDetail.swift

struct LandmarkDetail: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
LandmarkDetail()
}

#Preview {

Copy the contents of the `body` property from `ContentView` into `LandmarkDetail`.

struct LandmarkDetail: View {
var body: some View {
VStack {
MapView()
.frame(height: 300)

CircleImage()
.offset(y: -130)
.padding(.bottom, -130)

VStack(alignment: .leading) {
Text("Turtle Rock")
.font(.title)

HStack {
Text("Joshua Tree National Park")
Spacer()
Text("California")
}
.font(.subheadline)
.foregroundStyle(.secondary)

Divider()

Text("About Turtle Rock")
.font(.title2)
Text("Descriptive text goes here.")
}
.padding()

#Preview {

Change `ContentView` to instead display `LandmarkList`.

ContentView.swift

struct ContentView: View {
var body: some View {
LandmarkList()
}
}

#Preview {
ContentView()
}

In the next few steps, you’ll add navigation among your list and detail views.

Embed the dynamically generated list of landmarks in a `NavigationSplitView`.

The navigation split view takes a second input that’s a placeholder for the view that appears after someone makes a selection. On iPhone, the split view doesn’t need the placeholder, but on iPad the detail pane can be present before someone makes a selection, as you’ll see later in this tutorial.

struct LandmarkList: View {
var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
LandmarkRow(landmark: landmark)
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

struct LandmarkList: View {
var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
LandmarkRow(landmark: landmark)

Add the `navigationTitle(_:)` modifier to set the title of the navigation bar when displaying the list.

struct LandmarkList: View {
var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
LandmarkRow(landmark: landmark)
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

LandmarkRow(landmark: landmark)
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")

Inside the list’s closure, wrap the returned row in a `NavigationLink`, specifying the `LandmarkDetail` view as the destination.

struct LandmarkList: View {
var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
NavigationLink {
LandmarkDetail()
} label: {
LandmarkRow(landmark: landmark)
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

NavigationSplitView {
List(landmarks) { landmark in
NavigationLink {
LandmarkDetail()
} label: {
LandmarkRow(landmark: landmark)
}

You can try out the navigation directly in the preview. Tap a landmark to visit the detail page.

#Preview {

Section 7

## Pass data into child views

The `LandmarkDetail` view still uses hard-coded details to show its landmark. Just like `LandmarkRow`, the `LandmarkDetail` type and the views it comprises need to use a `landmark` property as the source for their data.

Starting with the child views, you’ll convert `CircleImage`, `MapView`, and then `LandmarkDetail` to display data that’s passed in, rather than hard-coding each row.

In the `CircleImage` file, add a stored `image` property to the `CircleImage` structure.

This is a common pattern when building views using SwiftUI. Your custom views will often wrap and encapsulate a series of modifiers for a particular view.

CircleImage.swift

struct CircleImage: View {
var image: Image

var body: some View {
image
.clipShape(Circle())
.overlay {
Circle().stroke(.white, lineWidth: 4)
}
.shadow(radius: 7)
}
}

#Preview {
CircleImage()
}

var body: some View {
image

Update the preview to pass the image of Turtle Rock.

Even though you’ve fixed the preview logic, the preview fails to update because the build fails. The detail view, which instantiates a circle image, needs an input parameter as well.

#Preview {
CircleImage(image: Image("turtlerock"))
}

#Preview {

In the `MapView` file, add a `coordinate` property to the `MapView` structure and update the preview to pass a fixed coordinate.

This change also affects the build because the detail view has a map view that needs the new parameter. You’ll fix the detail view soon.

MapView.swift

import SwiftUI
import MapKit

struct MapView: View {
var coordinate: CLLocationCoordinate2D

var body: some View {
Map(initialPosition: .region(region))
}

private var region: MKCoordinateRegion {
MKCoordinateRegion(
center: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868),
span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
)
}
}

#Preview {
MapView(coordinate: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868))
}

var body: some View {

Pass the coordinate to the center parameter in the region variable.

SwiftUI notices when the `coordinate` input to this view changes and evaluates the body again to update the view. That in turn recalculates the `region` using the new input value.

private var region: MKCoordinateRegion {
MKCoordinateRegion(
center: coordinate,
span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
)
}
}

#Preview {

private var region: MKCoordinateRegion {
MKCoordinateRegion(
center: coordinate,
span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
)

Change the map’s initializer to one that takes a position input so that it updates when the value changes.

This new initializer expects a `Binding` to a position, which is a bidirectional connection to the value. Use a `.constant()` binding here because `MapView` doesn’t need to detect when someone changes the position by interacting with the map.

var body: some View {
Map(position: .constant(.region(region)))
}

#Preview {

In `LandmarkDetail`, add a `Landmark` property to the `LandmarkDetail` type.

struct LandmarkDetail: View {
var landmark: Landmark

var body: some View {
VStack {
MapView()
.frame(height: 300)

#Preview {
LandmarkDetail(landmark: landmarks[0])
}

In `LandmarkList`, pass the current landmark to the destination `LandmarkDetail`.

struct LandmarkList: View {
var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

List(landmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)

In the `LandmarkDetail` file, pass the required data to your custom types.

With all of the connections established, the preview begins working again.

var body: some View {
VStack {
MapView(coordinate: landmark.locationCoordinate)
.frame(height: 300)

CircleImage(image: landmark.image)
.offset(y: -130)
.padding(.bottom, -130)

VStack(alignment: .leading) {
Text(landmark.name)
.font(.title)

HStack {
Text(landmark.park)
Spacer()
Text(landmark.state)
}
.font(.subheadline)
.foregroundStyle(.secondary)

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()

#Preview {

Change the container from a `VStack` to a `ScrollView` so the user can scroll through the descriptive content, and delete the `Spacer`, which you no longer need.

var body: some View {
ScrollView {
MapView(coordinate: landmark.locationCoordinate)
.frame(height: 300)

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
}
}
}

#Preview {

Finally, call the `navigationTitle(_:)` modifier to give the navigation bar a title when showing the detail view, and the `navigationBarTitleDisplayMode(_:)` modifier to make the title appear inline.

The navigation changes only have an effect when the view is part of a navigation stack.

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
}
.navigationTitle(landmark.name)
.navigationBarTitleDisplayMode(.inline)
}
}

#Preview {

.padding()
}
.navigationTitle(landmark.name)
.navigationBarTitleDisplayMode(.inline)
}
}

Go

#Preview {

Section 8

## Generate previews dynamically

Next, you’ll render previews of the list view for different device configurations.

By default, previews render at the size of the device in the active scheme. You can render for different devices by changing the target, or by overriding the device in the canvas. You can also explore other preview variations, like device orientation.

Change the device selector to make the preview display an iPad.

In portait orientation, the `NavigationSplitView` displays the detail pane by default, and provides a button in the toolbar to reveal the sidebar.

Tap the toolbar button to reveal the sidebar, and try navigating to one of the landmarks.

The detail view changes to the selected landmark under the sidebar. The sidebar remains visible until you tap somewhere in the detail view.

In the canvas, select the Device Settings and enable the Landscape Left orientation.

In landscape orientation, the `NavigationSplitView` displays the sidebar and detail panes side-by-side.

Experiment with different devices and configurations in the Device Settings to see how your views look under other conditions.

## Check Your Understanding

Question 1 of 4

In addition to `List`, which of these types presents a dynamic list of views from a collection?

Possible answers

`Group`

`ForEach`

`UITableView`

Submit Next question

Next

## Handling user input

In the Landmarks app, a user can flag their favorite places, and filter the list to show just their favorites. To create this feature, you’ll start by adding a switch to the list so users can focus on just their favorites, and then you’ll add a star-shaped button that a user taps to flag a landmark as a favorite.

Get started

---

# https://developer.apple.com/tutorials/swiftui/handling-user-input

SwiftUI essentials

# Handling user input

In the Landmarks app, a user can flag their favorite places, and filter the list to show just their favorites. To create this feature, you’ll start by adding a switch to the list so users can focus on just their favorites, and then you’ll add a star-shaped button that a user taps to flag a landmark as a favorite.

Download the starter project and follow along with this tutorial, or open the finished project and explore the code on your own.

20

mins

Section 1

## Mark favorite landmarks

Begin by enhancing the list to show people their favorites at a glance. Add a property to the `Landmark` structure to read the initial state of a landmark as a favorite, and then add a star to each `LandmarkRow` that shows a favorite landmark.

Step 1

Open the starting point Xcode project or the project you finished in the previous tutorial, and select `Landmark` in the Project navigator.

Step 2

Add an `isFavorite` property to the `Landmark` structure.

The `landmarkData` file has a key with this name for each landmark. Because `Landmark` conforms to `Codable`, you can read the value associated with the key by creating a new property with the same name as the key.

Landmark.swift

import Foundation
import SwiftUI
import CoreLocation

struct Landmark: Hashable, Codable, Identifiable {
var id: Int
var name: String
var park: String
var state: String
var description: String
var isFavorite: Bool

private var imageName: String
var image: Image {
Image(imageName)
}

private var coordinates: Coordinates
var locationCoordinate: CLLocationCoordinate2D {
CLLocationCoordinate2D(
latitude: coordinates.latitude,
longitude: coordinates.longitude)
}

struct Coordinates: Hashable, Codable {
var latitude: Double
var longitude: Double
}
}

var state: String
var description: String
var isFavorite: Bool

private var imageName: String

No Preview

Step 3

Select `LandmarkRow` in the Project navigator.

LandmarkRow.swift

import SwiftUI

struct LandmarkRow: View {
var landmark: Landmark

var body: some View {
HStack {
landmark.image
.resizable()
.frame(width: 50, height: 50)
Text(landmark.name)

Spacer()
}
}
}

#Preview {
Group {
LandmarkRow(landmark: landmarks[0])
LandmarkRow(landmark: landmarks[1])
}
}

#Preview {

Preview

Step 4

After the spacer, add a star image inside an `if` statement to test whether the current landmark is a favorite.

In SwiftUI blocks, you use `if` statements to conditionally include views.

Spacer()

if landmark.isFavorite {
Image(systemName: "star.fill")
}
}
}
}

#Preview {

if landmark.isFavorite {
Image(systemName: "star.fill")
}
}
}

Step 5

Because system images are vector based, you can change their color with the `foregroundStyle(_:)` modifier.

The star is present whenever a landmark’s `isFavorite` property is `true`. You’ll see how to modify that property later in this tutorial.

if landmark.isFavorite {
Image(systemName: "star.fill")
.foregroundStyle(.yellow)
}
}
}
}

#Preview {

if landmark.isFavorite {
Image(systemName: "star.fill")
.foregroundStyle(.yellow)
}
}

Section 2

## Filter the list view

You can customize the list view so that it shows all of the landmarks, or just the user’s favorites. To do this, you’ll need to add a bit of _state_ to the `LandmarkList` type.

_State_ is a value, or a set of values, that can change over time, and that affects a view’s behavior, content, or layout. You use a property with the `@State` attribute to add state to a view.

Select `LandmarkList` in the Project navigator.

LandmarkList.swift

struct LandmarkList: View {
var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {
LandmarkList()
}

#Preview {

Add a `@State` property called `showFavoritesOnly` with its initial value set to `false`.

Because you use state properties to hold information that’s specific to a view and its subviews, you always create state as `private`.

struct LandmarkList: View {
@State private var showFavoritesOnly = false

var body: some View {
NavigationSplitView {
List(landmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

var body: some View {
NavigationSplitView {

When you make changes to your view’s structure, like adding or modifying a property, the canvas automatically refreshes.

Compute a filtered version of the landmarks list by checking the `showFavoritesOnly` property and each `landmark.isFavorite` value.

var filteredLandmarks: [Landmark] {
landmarks.filter { landmark in
(!showFavoritesOnly || landmark.isFavorite)
}
}

#Preview {

@State private var showFavoritesOnly = false

Use the filtered version of the list of landmarks in the `List`.

var body: some View {
NavigationSplitView {
List(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

var body: some View {
NavigationSplitView {
List(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)

Step 6

Change the initial value of `showFavoritesOnly` to `true` to see how the list reacts.

struct LandmarkList: View {
@State private var showFavoritesOnly = true

#Preview {

var filteredLandmarks: [Landmark] {

#Preview {

Section 3

## Add a control to toggle the state

To give the user control over the list’s filter, you need to add a control that can alter the value of `showFavoritesOnly`. You do this by passing a binding to a toggle control.

A _binding_ acts as a reference to a mutable state. When a user taps the toggle from off to on, and off again, the control uses the binding to update the view’s state accordingly.

Create a nested `ForEach` group to transform the landmarks into rows.

To combine static and dynamic views in a list, or to combine two or more different groups of dynamic views, use the `ForEach` type instead of passing your collection of data to `List`.

var body: some View {
NavigationSplitView {
List {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

var body: some View {
NavigationSplitView {
List {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)

Add a `Toggle` view as the first child of the `List` view, passing a binding to `showFavoritesOnly`.

You use the `$` prefix to access a binding to a state variable, or one of its properties.

var body: some View {
NavigationSplitView {
List {
Toggle(isOn: $showFavoritesOnly) {
Text("Favorites only")
}

ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

NavigationSplitView {
List {
Toggle(isOn: $showFavoritesOnly) {
Text("Favorites only")
}

ForEach(filteredLandmarks) { landmark in
NavigationLink {

Improve the filtering animation by adding an `animation(_:)` modifier that begins when the `filteredLandmarks` value changes.

ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
} detail: {

Before moving on, return the default value of `showsFavoritesOnly` to `false`.

#Preview {

Use the Live preview and try out this new functionality by tapping the toggle.

Video with custom controls.

Play

#Preview {

Section 4

## Use observation for storage

To prepare for the user to control which particular landmarks are favorites, you’ll first store the landmark data using the `Observable()` macro.

With Observation, a view in SwiftUI can support data changes without using property wrappers or bindings. SwiftUI watches for any observable property changes that could affect a view, and displays the correct version of the view after a change.

In the project’s navigation pane, select `ModelData`.

ModelData.swift

import Foundation

var landmarks: [Landmark] = load("landmarkData.json")

let data: Data

guard let file = Bundle.main.url(forResource: filename, withExtension: nil)
else {
fatalError("Couldn't find \(filename) in main bundle.")
}

do {
data = try Data(contentsOf: file)
} catch {
fatalError("Couldn't load \(filename) from main bundle:\n\(error)")
}

do {
let decoder = JSONDecoder()
return try decoder.decode(T.self, from: data)
} catch {
fatalError("Couldn't parse \(filename) as \(T.self):\n\(error)")
}
}

Declare a new model type using the `Observable()` macro.

SwiftUI updates a view only when an observable property changes and the view’s body reads the property directly.

@Observable
class ModelData {
}

Move the `landmarks` array into the model.

@Observable
class ModelData {
var landmarks: [Landmark] = load("landmarkData.json")
}

Section 5

## Adopt the model object in your views

Now that you’ve created the `ModelData` object, you need to update your views to adopt it as the data store for your app.

In `LandmarkList`, add an `@Environment` property wrapper to the view, and an `environment(_:)` modifier to the preview.

The `modelData` property gets its value automatically, as long as the `environment(_:)` modifier has been applied to a parent. The `@Environment` property wrapper enables you to read the model data of the current view. Adding an `environment(_:)` modifier passes the data object down through the environment.

struct LandmarkList: View {
@Environment(ModelData.self) var modelData
@State private var showFavoritesOnly = false

#Preview {
LandmarkList()
.environment(ModelData())
}

Use `modelData.landmarks` as the data when filtering landmarks.

var filteredLandmarks: [Landmark] {
modelData.landmarks.filter { landmark in
(!showFavoritesOnly || landmark.isFavorite)
}
}

#Preview {

var filteredLandmarks: [Landmark] {
modelData.landmarks.filter { landmark in
(!showFavoritesOnly || landmark.isFavorite)
}

Update the `LandmarkDetail` view to work with the `ModelData` object in the environment.

LandmarkDetail.swift

struct LandmarkDetail: View {
var landmark: Landmark

var body: some View {
ScrollView {
MapView(coordinate: landmark.locationCoordinate)
.frame(height: 300)

CircleImage(image: landmark.image)
.offset(y: -130)
.padding(.bottom, -130)

VStack(alignment: .leading) {
Text(landmark.name)
.font(.title)

HStack {
Text(landmark.park)
Spacer()
Text(landmark.state)
}
.font(.subheadline)
.foregroundStyle(.secondary)

Divider()

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
}
.navigationTitle(landmark.name)
.navigationBarTitleDisplayMode(.inline)
}
}

#Preview {
LandmarkDetail(landmark: ModelData().landmarks[0])
}

#Preview {

Update the `LandmarkRow` preview to work with the `ModelData` object.

var body: some View {
HStack {
landmark.image
.resizable()
.frame(width: 50, height: 50)
.cornerRadius(5)
Text(landmark.name)

if landmark.isFavorite {
Image(systemName: "star.fill")
.imageScale(.medium)
.foregroundStyle(.yellow)
}
}
}
}

#Preview {
let landmarks = ModelData().landmarks
return Group {
LandmarkRow(landmark: landmarks[0])
LandmarkRow(landmark: landmarks[1])
}
}

#Preview {
let landmarks = ModelData().landmarks
return Group {
LandmarkRow(landmark: landmarks[0])
LandmarkRow(landmark: landmarks[1])

Update the `ContentView` preview to add the model object to the environment, which makes the object available to any subview.

A preview fails if any subview requires a model object in the environment, but the view you are previewing doesn’t have the `environment(_:)` modifier.

ContentView.swift

struct ContentView: View {
var body: some View {
LandmarkList()
}
}

#Preview {
ContentView()
.environment(ModelData())
}

#Preview {

Next, you’ll update the app instance to put the model object in the environment when you run the app in the simulator or on a device.

Update the `LandmarksApp` to create a model instance and supply it to `ContentView` using the `environment(_:)` modifier.

Use the `@State` attribute to initialize a model object the same way you use it to initialize properties inside a view. Just like SwiftUI initializes state in a view only once during the lifetime of the view, it initializes state in an app only once during the lifetime of the app.

LandmarksApp.swift

@main
struct LandmarksApp: App {
@State private var modelData = ModelData()

var body: some Scene {
WindowGroup {
ContentView()
.environment(modelData)
}
}
}

var body: some Scene {

Step 7

Switch

#Preview {

Section 6

## Create a favorite button for each landmark

The Landmarks app can now switch between a filtered and unfiltered view of the landmarks, but the list of favorite landmarks is still hard coded. To allow the user to add and remove favorites, you need to add a favorite button to the landmark detail view.

You’ll first create a reusable `FavoriteButton`.

Create a new view called `FavoriteButton.swift`.

FavoriteButton.swift

struct FavoriteButton: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
FavoriteButton()
}

#Preview {

Add an `isSet` binding that indicates the button’s current state, and provide a constant value for the preview.

The binding property wrapper enables you to read and write between a property that stores data and a view that displays and changes the data. Because you use a binding, changes made inside this view propagate

struct FavoriteButton: View {
@Binding var isSet: Bool

var body: some View {
Text("Hello, World!")

Create a `Button` with an action that toggles the `isSet` state, and that changes its appearance based on the state.

The title string that you provide for the button’s label doesn’t appear in the UI when you use the `iconOnly` label style, but VoiceOver uses it to improve accessibility.

var body: some View {
Button {
isSet.toggle()
} label: {
Label("Toggle Favorite", systemImage: isSet ? "star.fill" : "star")
.labelStyle(.iconOnly)
.foregroundStyle(isSet ? .yellow : .gray)
}
}
}

#Preview {
FavoriteButton(isSet: .constant(true))
}

As your project grows, it’s a good idea to add hierarchy. Before moving on, create a few more groups.

Collect the general purpose `CircleImage`, `MapView`, and `FavoriteButton` files into a Helpers group, and the landmark views into a Landmarks group.

Next, you’ll add the `FavoriteButton` to the detail view, binding the button’s `isSet` property to the `isFavorite` property of a given landmark.

Switch to `LandmarkDetail`, and compute the index of the input landmark by comparing it with the model data.

To support this, you also need access to the environment’s model data.

struct LandmarkDetail: View {
@Environment(ModelData.self) var modelData
var landmark: Landmark

var landmarkIndex: Int {
modelData.landmarks.firstIndex(where: { $0.id == landmark.id })!
}

#Preview {
let modelData = ModelData()
return LandmarkDetail(landmark: modelData.landmarks[0])
.environment(modelData)
}

Inside the body property, add the model data using a `Bindable` wrapper. Embed the landmark’s name in an `HStack` with a new `FavoriteButton`; provide a binding to the `isFavorite` property with the dollar sign (`$`).

Use `landmarkIndex` with the `modelData` object to ensure that the button updates the `isFavorite` property of the landmark stored in your model object.

var body: some View {
@Bindable var modelData = modelData

ScrollView {
MapView(coordinate: landmark.locationCoordinate)
.frame(height: 300)

VStack(alignment: .leading) {
HStack {
Text(landmark.name)
.font(.title)
FavoriteButton(isSet: $modelData.landmarks[landmarkIndex].isFavorite)
}

#Preview {

ScrollView {
MapView(coordinate: landmark.locationCoordinate)

#Preview {

## Check Your Understanding

Question 1 of 3

Which of the following passes data downward in the view hierarchy?

Possible answers

The `@Environment` property wrapper.

The `environment(_:)` modifier.

Submit Next question

Next

## Drawing paths and shapes

Users receive a badge whenever they visit a landmark in their list. Of course, for a user to receive a badge, you’ll need to create one. This tutorial takes you through the process of creating a badge by combining paths and shapes, which you then overlay with another shape that represents the location.

Get started

---

# https://developer.apple.com/tutorials/swiftui/creating-a-watchos-app

Framework integration

# Creating a watchOS app

This tutorial gives you a chance to apply much of what you’ve already learned about SwiftUI, and — with little effort — migrate the Landmarks app to watchOS.

You’ll start by adding a watchOS target to your project, before copying over the shared data and views you created for the iOS app. With all of the assets in place, you’ll customize the SwiftUI views to display the detail and list views on watchOS.

Follow the steps to build this project, or download the finished project to explore on your own.

25

mins

Section 1

## Add a watchOS target

To create a watchOS app, start by adding a watchOS target to the project. Xcode adds groups and files for the watchOS app to your project, along with the schemes needed to build and run the app.

Step 1

This template adds a new watchOS app to your project.

Step 2

In the sheet, enter WatchLandmarks as the Product Name. Select the Watch App for Existing iOS App, and then click Finish.

Step 3

When prompted by Xcode to activate the WatchLandmarks Watch App scheme, click Activate.

This enables you to start working with the new target.

Step 4

Select Apple Watch Series 9 (45mm) device in the watchOS Simulators dropdown.

Step 5

Select the WatchLandmarks Watch App target and navigate to the target’s General tab; select the Supports Running Without iOS App Installation checkbox.

Section 2

## Share files between targets

With the watchOS target set, you’ll need to share some resources from the iOS target. You’ll reuse the Landmark app’s data model, some resource files, as well as any views that both platforms can display without modification.

First, delete the entry point for the watchOS app. You don’t need it because you’ll reuse the entry point defined in `LandmarksApp` instead.

In the Project navigator, delete the `WatchLandmarksApp` file in the WatchLandmarks Watch App folder; When asked, choose Move to trash.

Next select all the files, including the app’s entry point, that your watchOS target can share with the existing iOS target.

In the Project navigator, Command-click to select the following files: `LandmarksApp`, `LandmarkList`, `LandmarkRow`, `CircleImage`, `MapView`.

The first of these is the shared app definition. The others are views that the app can display on watchOS with no changes.

Continue Command-clicking to add the following model files: `ModelData`, `Landmark`, `Hike`, `Profile`.

These items define the app’s data model. You won’t use all aspects of the model, but you need all of the files to successfully compile the app.

Finish Command-clicking to add resource files loaded by the model: `landmarkData`, `hikeData`, and `Assets`.

In the File inspector, select the WatchLandmarks Watch App checkbox in the Target Membership section.

This makes the symbols you selected in the previous steps available to your watchOS app.

Finally, add a watchOS app icon that matches the iOS app icon you already have.

Step 6

Select the `Assets` file in the WatchLandmarks Watch App folder and navigate to the empty AppIcon item.

Step 7

Drag the single png file from the downloaded project’s Resources folder into the existing empty AppIcon set.

Later, when you create a notification, the system presents your app’s icon to help identify the source of the notification.

Section 3

## Create the detail view

Now that the iOS target resources are in place for working on the watch app, you’ll need to create a watch-specific view for displaying landmark details. To test the detail view, you’ll create custom previews for the largest and smallest watch sizes, and make some changes to the circle view so everything fits on the watch face.

Add a new custom view to the WatchLandmarks Watch App folder named `LandmarkDetail.swift`.

This file is distinguished from the file with the same name in the iOS project by its target membership — it applies only to the WatchLandmarks Watch App target.

Add the `modelData`, `landmark`, and `landmarkIndex` properties to the new `LandmarkDetail` structure.

These are identical to the properties you added in Handling user input.

LandmarkDetail.swift

import SwiftUI

struct LandmarkDetail: View {
@Environment(ModelData.self) var modelData
var landmark: Landmark

var landmarkIndex: Int {
modelData.landmarks.firstIndex(where: { $0.id == landmark.id })!
}

var body: some View {
Text("Hello, World!")
}
}

#Preview {
LandmarkDetail()
}

var body: some View {
Text("Hello, World!")

No Preview

In the preview, create an instance of the model data, and use it to pass a landmark object to the `LandmarkDetail` structure’s initializer. You also need to set the view’s environment.

#Preview {
let modelData = ModelData()
return LandmarkDetail(landmark: modelData.landmarks[0])
.environment(modelData)
}

#Preview {

Preview

Set the device selector to make the preview display a Large Watch.

Return a `CircleImage` view from the `body()` method.

Here you reuse the `CircleImage` view from the iOS project. Because you created a resizable image, the call to `scaledToFill()` adjusts the circle’s size so that it fills the display.

var body: some View {
CircleImage(image: landmark.image.resizable())
.scaledToFill()
}
}

#Preview {

Change the device selector to make the preview display a Small Watch.

By testing against the largest and smallest watch faces, you can see how well your app scales to fit on the display. As always, you should test your user interface on all supported device sizes.

#Preview {

#Preview {

Embed the circle image in a `VStack`. Display the landmark name and its information below the image.

As you can see, the information doesn’t quite fit on the watch screen, but you can fix that by placing the `VStack` within a scroll view.

var body: some View {
@Bindable var modelData = modelData

VStack {
CircleImage(image: landmark.image.resizable())
.scaledToFill()

Text(landmark.name)
.font(.headline)
.lineLimit(0)

Toggle(isOn: $modelData.landmarks[landmarkIndex].isFavorite) {
Text("Favorite")
}

Divider()

Text(landmark.park)
.font(.caption)
.bold()
.lineLimit(0)

Text(landmark.state)
.font(.caption)
}
}
}

#Preview {

Step 8

Wrap the vertical stack in a scroll view.

This turns on view scrolling, but it creates another problem: the circle image now expands to full size, and it resizes other UI elements to match the image size. You’ll need to resize the circle image so that just the circle and landmark name appear onscreen.

ScrollView {
VStack {
CircleImage(image: landmark.image.resizable())
.scaledToFill()

Text(landmark.state)
.font(.caption)
}
}
}
}

#Preview {

@Bindable var modelData = modelData

ScrollView {
VStack {
CircleImage(image: landmark.image.resizable())

Step 9

Change `scaleToFill()` to `scaleToFit()` and add padding.

This scales the circle image to match the display’s width and ensures the landmark name is visible below the circle image.

ScrollView {
VStack {
CircleImage(image: landmark.image.resizable())
.scaledToFit()

Text(landmark.state)
.font(.caption)
}
.padding(16)
}
}
}

#Preview {

VStack {
CircleImage(image: landmark.image.resizable())
.scaledToFit()

Text(landmark.name)

Step 10

Add the `MapView` after a divider.

The map appears off screen, but you can scroll down to see it.

Text(landmark.state)
.font(.caption)

MapView(coordinate: landmark.locationCoordinate)
.scaledToFit()
}
.padding(16)
}
}
}

#Preview {

MapView(coordinate: landmark.locationCoordinate)
.scaledToFit()
}
.padding(16)

Step 11

Add a title to the back button.

This sets the text for the back button to “Landmarks”.

MapView(coordinate: landmark.locationCoordinate)
.scaledToFit()
}
.padding(16)
}
.navigationTitle("Landmarks")
}
}

#Preview {

.padding(16)
}
.navigationTitle("Landmarks")
}
}

Section 4

## Add the landmarks list

The `LandmarkList` that you created for iOS works for your watch app as well, and it automatically navigates to the watch-specific detail view that you just created when compiled for watchOS. Next, you’ll connect the list to the watch’s `ContentView`, so that it acts as the top level view for the watch app.

Select `ContentView` in the WatchLandmarks Watch App folder.

Like `LandmarkDetail` the content view for the watchOS target has the same name as the one for the iOS target. Keeping names and interfaces the same makes it easy to share files between targets.

ContentView.swift

struct ContentView: View {
var body: some View {
VStack {
Image(systemName: "globe")
.imageScale(.large)
.foregroundStyle(.tint)
Text("Hello, world!")
}
.padding()
}
}

#Preview {
ContentView()
}

#Preview {

The watchOS app’s root view displays the default “Hello, World!” message.

Modify `ContentView` so that it displays the List view.

Be sure to provide the model data as an environment to the preview. The `LandmarksApp` already provides this at the app level at run time, just as it does for iOS, but you also have to provide it for any previews that need it.

struct ContentView: View {
var body: some View {
LandmarkList()
}
}

#Preview {
ContentView()
.environment(ModelData())
}

Make sure you are on the Live preview to check out how the app behaves.

Video with custom controls.

Content description: A screen recording of the Live preview of the watch app showing how you can navigate from the list of landmarks to the detail view for one of them, including an interactive map.

Play

#Preview {

Section 5

## Create a custom notification interface

Your version of Landmarks for watchOS is almost complete. In this final section, you’ll create a notification interface that displays landmark information whenever you receive a notification indicating that you are close to one of your favorite locations.

Add a new custom view to the WatchLandmarks Watch App folder named `NotificationView.swift` and create a view that displays information about a landmark, title, and message.

NotificationView.swift

struct NotificationView: View {
var title: String?
var message: String?
var landmark: Landmark?

var body: some View {
VStack {
if let landmark {
CircleImage(image: landmark.image.resizable())
.scaledToFit()
}

Text(title ?? "Unknown Landmark")
.font(.headline)

Text(message ?? "You are within 5 miles of one of your favorite landmarks.")
.font(.caption)
}
}
}

#Preview {
NotificationView()
}

var body: some View {
VStack {

Add a preview that sets the title, message, and landmark properties for the notification view.

This shows a preview of the notification view when data is provided. Because any notification value can be `nil`, it’s useful to keep the default preview of the notification view when no data is provided.

#Preview {

#Preview {
NotificationView(
title: "Turtle Rock",
message: "You are within 5 miles of Turtle Rock.",
landmark: ModelData().landmarks[0])
}

#Preview {

Create a new Swift file called `NotificationController.swift`, and add a hosting controller structure that include the `landmark`, `title`, and `message` properties.

These properties store values about an incoming notification.

NotificationController.swift

import WatchKit
import SwiftUI
import UserNotifications

var landmark: Landmark?
var title: String?
var message: String?

override var body: NotificationView {
NotificationView()
}
}

Update the `body()` method to use these properties.

This method instantiates the notification view that you created earlier.

override var body: NotificationView {
NotificationView(
title: title,
message: message,
landmark: landmark
)
}
}

Define the `landmarkIndexKey`.

You use this key to extract the landmark index from the notification.

let landmarkIndexKey = "landmarkIndex"

var message: String?

override var body: NotificationView {
NotificationView(

Add the `didReceive(_:)` method to parse data from the notification.

This method updates the controller’s properties. After calling this method, the system invalidates the controller’s `body` property, which updates your notification view. The system then displays the notification on Apple Watch.

override var body: NotificationView {
NotificationView(
title: title,
message: message,
landmark: landmark
)
}

override func didReceive(_ notification: UNNotification) {
let modelData = ModelData()

let notificationData =
notification.request.content.userInfo as? [String: Any]

let aps = notificationData?["aps"] as? [String: Any]
let alert = aps?["alert"] as? [String: Any]

title = alert?["title"] as? String
message = alert?["body"] as? String

if let index = notificationData?[landmarkIndexKey] as? Int {
landmark = modelData.landmarks[index]
}
}
}

)
}

When Apple Watch receives a notification, it looks for a scene in your app associated with the notification’s category.

Go to `LandmarksApp` and add a `WKNotificationScene` using the `LandmarkNear` category.

The scene only makes sense for watchOS, so add the conditional compilation.

LandmarksApp.swift

@main
struct LandmarksApp: App {
@State private var modelData = ModelData()

var body: some Scene {
WindowGroup {
ContentView()
.environment(modelData)
}

#if os(watchOS)
WKNotificationScene(controller: NotificationController.self, category: "LandmarkNear")
#endif
}
}

}

#if os(watchOS)
#endif
WKNotificationScene(controller: NotificationController.self, category: "LandmarkNear")
}
}

Before your app can show alerts, it needs to request permission to do so.

Go to `ContentView` and request authorization to enable notifications from Notification Center.

You make the request using an asynchronous task modifier that SwiftUI calls when the content view first appears.

import SwiftUI
import UserNotifications

struct ContentView: View {
var body: some View {
LandmarkList()
.task {
let center = UNUserNotificationCenter.current()
_ = try? await center.requestAuthorization(
options: [.alert, .sound, .badge]
)
}
}
}

#Preview {

struct ContentView: View {

Configure the test payload to use the `LandmarkNear` category and to pass along the data expected by the notification controller.

Add a new Notification Simulation File to the WatchLandmarks Watch App folder named `PushNotificationPayload.apns`.

Don’t add the `PushNotificationPayload` file to any target, because it isn’t part of the app.

Update the `title`, `body`, `category`, `landmarkIndex` and `Simulator Target Bundle` properties. Be sure to set `category` to `LandmarkNear`. You also delete any keys that are not used in the tutorial, such as the `subtitle`, `WatchKit Simulator Actions`, and `customKey`.

The payload file simulates data sent from your server in a remote notification.

PushNotificationPayload.apns

{
"aps": {
"alert": {
"title": "Silver Salmon Creek",
"body": "You are within 5 miles of Silver Salmon Creek."
},
"category": "LandmarkNear",
"thread-id": "5280"
},

"landmarkIndex": 1,

"Simulator Target Bundle": "com.example.apple-samplecode.Landmarks.watchkitapp"
}

"aps": {
"alert": {
"title": "Silver Salmon Creek",
"body": "You are within 5 miles of Silver Salmon Creek."
},
"category": "LandmarkNear",

Build and run the WatchLandmarks Watch App scheme on a Simulator.

The first time you run the app, the system asks for permission to send notifications. Select Allow.

Content description: A video of the app asking permission to show notifications.

Step 12

After you grant permission, use Xcode to stop the app, and then drag the `PushNotificationPayload` file over the watch face.

Content description: A video of the notification showing up in the Simulator.

The Simulator displays a scrollable notification which includes: the app’s icon to help identify the Landmarks app as the sender, the notification view, and buttons for the notification’s actions.

#Preview {

## Check Your Understanding

Question 1 of 2

Which option do you use when adding a WatchOS target to an existing iOS project?

Possible answers

Watch-only App

Watch App with New Companion iOS App

Watch App for Existing iOS App

Submit Next question

Next

## Creating a macOS app

After creating a version of the Landmarks app for watchOS, it’s time to set your sights on something bigger: bringing Landmarks to the Mac. You’ll build upon everything you’ve learned so far, to round out the experience of building a SwiftUI app for iOS, watchOS, and macOS.

Get started

---

# https://developer.apple.com/tutorials/swiftui/creating-a-macos-app

Framework integration

# Creating a macOS app

After creating a version of the Landmarks app for watchOS, it’s time to set your sights on something bigger: bringing Landmarks to the Mac. You’ll build upon everything you’ve learned so far, to round out the experience of building a SwiftUI app for iOS, watchOS, and macOS.

You’ll start by adding a macOS target to your project, and then reusing views and data you created earlier. With a foundation in place, you’ll add some new views tailored to macOS, and modify others to work better across platforms.

Follow the steps to build this project, or download the finished project to explore on your own.

30

mins

Section 1

## Add a macOS target to the project

Start by adding a macOS target to the project. Xcode adds a new group and set of starter files for the macOS app, along with the scheme needed to build and run the app. You’ll then add some existing files to the new target.

To be able to preview and run the app, be sure your Mac is running macOS Sonoma or later.

Step 1

This template adds a new macOS app target to the project.

Step 2

In the sheet, enter `MacLandmarks` as the Product Name. Set the interface to SwiftUI and the language to Swift, and then click Finish.

Step 3

By setting the scheme to My Mac, you can preview, build, and run the macOS app. As you move through the tutorial, you’ll use the other schemes to keep an eye on how other targets respond to changes in shared files.

Step 4

In the MacLandmarks group, select `ContentView`, open the Canvas to see the preview.

SwiftUI provides both a default main view and its preview, just like for an iOS app, enabling you to preview the app’s main window.

ContentView.swift

import SwiftUI

struct ContentView: View {
var body: some View {
Text("Hello, world!")
.padding()
}
}

#Preview {
ContentView()
}

#Preview {

Preview

Step 5

In the Project navigator, delete the `MacLandmarksApp` file from the MacLandmarks group. When asked, choose Move to Trash.

Like with the watchOS app, you don’t need the default app structure because you’ll reuse the one you already have.

Next, you’ll share view, model, and resource files from the iOS app with the macOS target.

Step 6

In the Project navigator, Command-click to select the following files: `LandmarksApp`, `LandmarkList`, `LandmarkRow`, `CircleImage`, `MapView`, and `FavoriteButton`.

The first of these is the shared app definition. The others are views that will work on macOS.

Step 7

Continue Command-clicking to select all the items in the Model and Resources folders, as well as `Asset`.

These items define the app’s data model and resources.

Step 8

In the File inspector, add MacLandmarks to the Target Membership for the selected files.

Add a macOS app icon set to match those for the other targets.

Step 9

Select the `Assets` file in the MacLandmarks group and delete the empty AppIcon item.

You’ll replace this in the next step.

Step 10

Drag the `AppIcon.appiconset` folder from the downloaded projects’ `Resources` folder into the MacLandmark’s Asset catalog.

Step 11

In `ContentView` in the MacLandmarks group, add `LandmarkList` as the top level view, with constraints on the frame size.

The preview no longer builds because the `LandmarkList` uses `LandmarkDetail`, but you haven’t defined a detail view for the macOS app yet. You’ll take care of that in the next section.

struct ContentView: View {
var body: some View {
LandmarkList()
.frame(minWidth: 700, minHeight: 300)
}
}

#Preview {
ContentView()
.environment(ModelData())
}

No Preview

Section 2

## Create a macOS detail view

The detail view displays information about the selected landmark. You created a view like this for the iOS app, but different platforms require different approaches to data presentation.

Sometimes you can reuse a view across platforms with small adjustments or conditional compilation, but the detail view differs enough for macOS that it’s better to create a dedicated view. You’ll copy the iOS detail view as a starting point, and then modify it to suit the larger display of macOS.

Create a new custom view in the MacLandmarks group targeting macOS called `LandmarkDetail`.

You now have three files called `LandmarkDetail`. Each serves the same purpose in the view hierarchy, but provides an experience tailored to a particular platform.

Copy the iOS detail view contents into the macOS detail view.

The preview fails because the `navigationBarTitleDisplayMode(_:)` method isn’t available in macOS.

LandmarkDetail.swift

struct LandmarkDetail: View {
@Environment(ModelData.self) var modelData
var landmark: Landmark

var landmarkIndex: Int {
modelData.landmarks.firstIndex(where: { $0.id == landmark.id })!
}

var body: some View {
@Bindable var modelData = modelData

ScrollView {
MapView(coordinate: landmark.locationCoordinate)
.frame(height: 300)

CircleImage(image: landmark.image)
.offset(y: -130)
.padding(.bottom, -130)

VStack(alignment: .leading) {
HStack {
Text(landmark.name)
.font(.title)
FavoriteButton(isSet: $modelData.landmarks[landmarkIndex].isFavorite)
}

HStack {
Text(landmark.park)
Spacer()
Text(landmark.state)
}
.font(.subheadline)
.foregroundStyle(.secondary)

Divider()

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
}
.navigationTitle(landmark.name)
.navigationBarTitleDisplayMode(.inline)
}
}

#Preview {
let modelData = ModelData()
return LandmarkDetail(landmark: modelData.landmarks[0])
.environment(modelData)
}

Delete the `navigationBarTitleDisplayMode(_:)` modifier and add a frame modifier to the preview so you can see more of the content.

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
}
.navigationTitle(landmark.name)
}
}

#Preview {
let modelData = ModelData()
return LandmarkDetail(landmark: modelData.landmarks[0])
.environment(modelData)
.frame(width: 850, height: 700)
}

return LandmarkDetail(landmark: modelData.landmarks[0])
.environment(modelData)
.frame(width: 850, height: 700)
}

The changes you’ll make in the next few steps improve the layout for the larger display of a Mac.

Change the `HStack` holding the park and state to a `VStack` with leading alignment, and remove the `Spacer`.

VStack(alignment: .leading) {
Text(landmark.park)
Text(landmark.state)
}
.font(.subheadline)
.foregroundStyle(.secondary)

#Preview {

}

VStack(alignment: .leading) {
Text(landmark.park)
Text(landmark.state)

Enclose everything below `MapView` in a `VStack`, and then place the `CircleImage` and the rest of the header in an `HStack`.

VStack(alignment: .leading, spacing: 20) {
HStack(spacing: 24) {
CircleImage(image: landmark.image)
.offset(y: -130)
.padding(.bottom, -130)

VStack(alignment: .leading) {
Text(landmark.park)
Text(landmark.state)
}
.font(.subheadline)
.foregroundStyle(.secondary)
}
}

#Preview {

.frame(height: 300)

VStack(alignment: .leading, spacing: 20) {
HStack(spacing: 24) {
CircleImage(image: landmark.image)
.offset(y: -130)

Remove the offset from the circle, and instead apply a smaller offset to the entire `VStack`.

VStack(alignment: .leading, spacing: 20) {
HStack(spacing: 24) {
CircleImage(image: landmark.image)

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
.offset(y: -50)
}
.navigationTitle(landmark.name)
}
}

#Preview {

}
.padding()
.offset(y: -50)
}
.navigationTitle(landmark.name)

Add a `resizable()` modifier to the image, and constrain the `CircleImage` to be a bit smaller.

VStack(alignment: .leading, spacing: 20) {
HStack(spacing: 24) {
CircleImage(image: landmark.image.resizable())
.frame(width: 160, height: 160)

#Preview {

VStack(alignment: .leading) {

Constrain the `ScrollView` to a maximum width.

This improves readability when the user makes the window very wide.

Text("About \(landmark.name)")
.font(.title2)
Text(landmark.description)
}
.padding()
.frame(maxWidth: 700)
.offset(y: -50)
}
.navigationTitle(landmark.name)
}
}

#Preview {

}
.padding()
.frame(maxWidth: 700)
.offset(y: -50)
}

Change the `FavoriteButton` to use the `plain` button style.

Using the plain style here makes the button look more like the iOS equivalent.

VStack(alignment: .leading) {
HStack {
Text(landmark.name)
.font(.title)
FavoriteButton(isSet: $modelData.landmarks[landmarkIndex].isFavorite)
.buttonStyle(.plain)
}

#Preview {

.font(.title)
FavoriteButton(isSet: $modelData.landmarks[landmarkIndex].isFavorite)
.buttonStyle(.plain)
}

The larger display gives you more room for additional features.

Add an “Open in Maps” button in a `ZStack` so that it appears on top of the map in the upper-right corner.

Be sure to include MapKit to be able to create the `MKMapItem` that you send to Maps.

import SwiftUI
import MapKit

ScrollView {
ZStack(alignment: Alignment(horizontal: .trailing, vertical: .top)) {
MapView(coordinate: landmark.locationCoordinate)
.frame(height: 300)

Button("Open in Maps") {
let destination = MKMapItem(placemark: MKPlacemark(coordinate: landmark.locationCoordinate))
destination.name = landmark.name
destination.openInMaps()
}
.padding()
}

#Preview {

struct LandmarkDetail: View {

Section 3

## Update the row view

The shared `LandmarkRow` view works in macOS, but it’s worth revisiting to look for improvements given the new visual environment. Because this view is used by all three platforms, you need to be careful that any changes you make work across all of them.

Before modifying the row, set up a preview of the list, because the changes you’ll make are driven by how the row looks in context.

Open `LandmarkList` and add a minimum width.

This improves the preview, but also ensures that the list never becomes too small as the user resizes the macOS window.

LandmarkList.swift

struct LandmarkList: View {
@Environment(ModelData.self) var modelData
@State private var showFavoritesOnly = false

var filteredLandmarks: [Landmark] {
modelData.landmarks.filter { landmark in
(!showFavoritesOnly || landmark.isFavorite)
}
}

var body: some View {
NavigationSplitView {
List {
Toggle(isOn: $showFavoritesOnly) {
Text("Favorites only")
}

ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
.frame(minWidth: 300)
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {
LandmarkList()
.environment(ModelData())
}

.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
.frame(minWidth: 300)
} detail: {
Text("Select a Landmark")

Pin the list view preview so that you can see how the row looks in context as you make changes.

Open `LandmarkRow` and add a corner radius to the image for a more refined look.

LandmarkRow.swift

struct LandmarkRow: View {
var landmark: Landmark

var body: some View {
HStack {
landmark.image
.resizable()
.frame(width: 50, height: 50)
.cornerRadius(5)
Text(landmark.name)

Spacer()

if landmark.isFavorite {
Image(systemName: "star.fill")
.imageScale(.medium)
.foregroundStyle(.yellow)
}
}
}
}

#Preview {
let landmarks = ModelData().landmarks
return Group {
LandmarkRow(landmark: landmarks[0])
LandmarkRow(landmark: landmarks[1])
}
}

.resizable()
.frame(width: 50, height: 50)
.cornerRadius(5)
Text(landmark.name)

Wrap the landmark name in a `VStack` and add the park as secondary information.

var body: some View {
HStack {
landmark.image
.resizable()
.frame(width: 50, height: 50)
.cornerRadius(5)
VStack(alignment: .leading) {
Text(landmark.name)
.bold()
Text(landmark.park)
.font(.caption)
.foregroundStyle(.secondary)
}

#Preview {

.frame(width: 50, height: 50)
.cornerRadius(5)
VStack(alignment: .leading) {
Text(landmark.name)
.bold()

Add vertical padding around the contents of the row to give each row a little more breathing room.

if landmark.isFavorite {
Image(systemName: "star.fill")
.imageScale(.medium)
.foregroundStyle(.yellow)
}
}
.padding(.vertical, 4)
}
}

#Preview {

}
}
.padding(.vertical, 4)
}
}

The updates improve the look in macOS, but you also need to consider the other platforms that use the list. Consider watchOS first.

Choose the WatchLandmarks target to see a watchOS preview of the list.

The minimum row width isn’t appropriate here. Because of this and other changes you’ll make to the list in the next section, the best solution is to create a watch-specific list that omits the width constraint.

#Preview {

#Preview {

Add a new SwiftUI view to the WatchLandmarks Watch App folder called `LandmarkList.swift` that targets only WatchLandmarks Watch App, and remove the older file’s WatchLandmarks Watch App target membership.

Copy the contents of the old `LandmarkList` into the new one, but without the frame modifier.

The content now has the right width, but each row has too much information.

ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

#Preview {

Go
LandmarkRow(landmark: landmarks[1])
}
}

Text(landmark.name)
.bold()
#if !os(watchOS)
Text(landmark.park)
.font(.caption)

Finally, consider how your changes work for iOS.

Choose the Landmarks build target to see what the list looks like for iOS.

The changes work well for iOS, so there’s no need to make any updates for that platform.

#Preview {

Section 4

## Update the list view

Like `LandmarkRow`, `LandmarkList` already works on macOS, but could use improvements. For example, you’ll move the toggle for showing only favorites to a menu in the toolbar, where it can be joined by additional filtering controls.

The changes you’ll make will work for both macOS and iOS, but will be difficult to accommodate on watchOS. Fortunately, in the previous section you already split the list into a separate file for watchOS.

var modelData
@State private var showFavoritesOnly = false

ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {

} label: {
Label("Filter", systemImage: "slider.horizontal.3")
}
}
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

.navigationTitle("Landmarks")
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {

} label: {
Label("Filter", systemImage: "slider.horizontal.3")
}
}
}
} detail: {
Text("Select a Landmark")

Move the favorites `Toggle` into the menu.

This moves the toggle into the toolbar in a platform-specific way, which has the additional benefit of making it accessible no matter how long the list of landmarks gets, or how far down the user scrolls.

var body: some View {
NavigationSplitView {
List {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {
Toggle(isOn: $showFavoritesOnly) {
Label("Favorites only", systemImage: "star.fill")
}
} label: {
Label("Filter", systemImage: "slider.horizontal.3")
}
}
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

ToolbarItem {
Menu {
Toggle(isOn: $showFavoritesOnly) {
Label("Favorites only", systemImage: "star.fill")
}
} label: {
Label("Filter", systemImage: "slider.horizontal.3")

With more room available, you’ll add a new control for filtering the list of landmarks by category.

Add a `FilterCategory` enumeration to describe filter states.

Match the case strings to the `Category` enumeration in the `Landmark` structure so that you can compare them, and include an `all` case to turn filtering off.

enum FilterCategory: String, CaseIterable, Identifiable {
case all = "All"
case lakes = "Lakes"
case rivers = "Rivers"
case mountains = "Mountains"

var id: FilterCategory { self }
}

#Preview {

@State private var showFavoritesOnly = false

var filteredLandmarks: [Landmark] {
modelData.landmarks.filter { landmark in

Add a `filter` state variable, defaulting to the `all` case.

By storing the filter state in the list view, the user can open multiple list view windows, each with its own filter setting, to be able to look at the data in different ways.

struct LandmarkList: View {
@Environment(ModelData.self) var modelData
@State private var showFavoritesOnly = false
@State private var filter = FilterCategory.all

#Preview {

@Environment(ModelData.self) var modelData
@State private var showFavoritesOnly = false
@State private var filter = FilterCategory.all

enum FilterCategory: String, CaseIterable, Identifiable {

Update `filteredLandmarks` to take into account the new `filter` setting, combined with the category of a given landmark.

var filteredLandmarks: [Landmark] {
modelData.landmarks.filter { landmark in
(!showFavoritesOnly || landmark.isFavorite)
&& (filter == .all || filter.rawValue == landmark.category.rawValue)
}
}

#Preview {

modelData.landmarks.filter { landmark in
(!showFavoritesOnly || landmark.isFavorite)
&& (filter == .all || filter.rawValue == landmark.category.rawValue)
}
}

Add a `Picker` to the menu to set the filter category.

Because the filter has only a few items, you use the `inline` picker style to make them all appear together.

var body: some View {
NavigationSplitView {
List {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle("Landmarks")
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {
Picker("Category", selection: $filter) {
ForEach(FilterCategory.allCases) { category in
Text(category.rawValue).tag(category)
}
}
.pickerStyle(.inline)

Toggle(isOn: $showFavoritesOnly) {
Label("Favorites only", systemImage: "star.fill")
}
} label: {
Label("Filter", systemImage: "slider.horizontal.3")
}
}
}
} detail: {
Text("Select a Landmark")
}
}
}

#Preview {

ToolbarItem {
Menu {
Picker("Category", selection: $filter) {
ForEach(FilterCategory.allCases) { category in
Text(category.rawValue).tag(category)
}
}
.pickerStyle(.inline)

Toggle(isOn: $showFavoritesOnly) {
Label("Favorites only", systemImage: "star.fill")

Update the navigation title to match the state of the filter.

This change will be useful in the iOS app.

var title: String {
let title = filter == .all ? "Landmarks" : filter.rawValue
return showFavoritesOnly ? "Favorite \(title)" : title
}

var body: some View {
NavigationSplitView {
List {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle(title)
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {
Picker("Category", selection: $filter) {
ForEach(FilterCategory.allCases) { category in
Text(category.rawValue).tag(category)
}
}
.pickerStyle(.inline)

#Preview {

var body: some View {
NavigationSplitView {

Run the macOS target and see how the menu operates.

Video with custom controls.

Content description: A video showing the MacLandmarks app running, trying out different filter options available in the menu.

Play

Choose the Landmarks build target, and make sure you are on the Live preview to see that the new filtering works well for iOS as well.

#Preview {

Section 5

## Add a built-in menu command

When you create an app using the SwiftUI life cycle, the system automatically creates a menu with commonly needed items, like those for closing the front-most window or for quitting the app. SwiftUI lets you add other common commands with built-in behavior, as well as completely custom commands.

In this section, you’ll add a system-provided command that lets the user toggle the sidebar, to be able to get it back after dragging it closed.

Add a new Swift file called `LandmarkCommands.swift` and set its targets to include both macOS and iOS.

You also target iOS because the shared `LandmarkList` will eventually depend on some of the types you define in this file.

Import SwiftUI and add a `LandmarkCommands` structure that conforms to the `Commands` protocol, with a computed body property.

Like a `View` structure, a `Commands` structure requires a computed body property that uses builder semantics, except with commands instead of views.

LandmarkCommands.swift

struct LandmarkCommands: Commands {
var body: some Commands {
}
}

struct LandmarkCommands: Commands {

Add a `SidebarCommands` command to the body.

This built-in command set includes the command for toggling the sidebar.

struct LandmarkCommands: Commands {
var body: some Commands {
SidebarCommands()
}
}

To make use of commands in an app, you have to apply them to a scene, which you’ll do next.

Open the `LandmarksApp` file, and apply `LandmarkCommands` using the `commands(content:)` scene modifier.

Scene modifiers work like view modifiers, except that you apply them to scenes instead of views.

LandmarksApp.swift

@main
struct LandmarksApp: App {
@State private var modelData = ModelData()

var body: some Scene {
WindowGroup {
ContentView()
.environment(modelData)
}
.commands {
LandmarkCommands()
}

#if os(watchOS)
WKNotificationScene(controller: NotificationController.self, category: "LandmarkNear")
#endif
}
}

.environment(modelData)
}
.commands {
LandmarkCommands()
}

#if os(watchOS)

Content description: A video showing the selection of Show Sidebar item from the View item in the MacLandmarks menu, which causes the app's sidebar to reappear.

Unfortunately, the watchOS app fails to build because `Commands` has no watchOS availability. You’ll fix that next.

Add a condition around the commands modifier to omit it for the watchOS app.

The watchOS app builds again.

var body: some Scene {
WindowGroup {
ContentView()
.environment(modelData)
}
#if !os(watchOS)
.commands {
LandmarkCommands()
}

#if os(watchOS)
#endif
WKNotificationScene(controller: NotificationController.self, category: "LandmarkNear")
}
}

.environment(modelData)
}
#if !os(watchOS)
.commands {
LandmarkCommands()

Content description: A video showing the MacLandmarks app's sidebar dragged to the left until it disappears.

Section 6

## Add a custom menu command

In the previous section, you added a built-in menu command set. In this section, you’ll add a custom command for toggling the favorite status of the currently selected landmark. To know which landmark is currently selected, you’ll use a focused binding.

In `LandmarkCommands`, extend the `FocusedValues` structure with a `selectedLandmark` value, using a custom key called `SelectedLandmarkKey`.

The pattern for defining focused values resembles the pattern for defining new `Environment` values: Use a private key to read and write a custom property on the system-defined `FocusedValues` structure.

private struct SelectedLandmarkKey: FocusedValueKey {

extension FocusedValues {

get { self[SelectedLandmarkKey.self] }
set { self[SelectedLandmarkKey.self] = newValue }
}
}

Add a `@FocusedBinding` property wrapper to track the currently selected landmark.

You’re reading the value here. You’ll set it later in the list view, where the user makes the selection.

struct LandmarkCommands: Commands {
@FocusedBinding(\.selectedLandmark) var selectedLandmark

var body: some Commands {
SidebarCommands()
}
}

var body: some Commands {
SidebarCommands()

Add a new `CommandMenu` to your commands called Landmarks.

You’ll define content for the menu next.

CommandMenu("Landmark") {
}
}
}

Add a button to the menu that toggles the selected landmark’s favorite status, and that has an appearance that changes depending on the currently selected landmark and its state.

CommandMenu("Landmark") {
Button("\(selectedLandmark?.isFavorite == true ? "Remove" : "Mark") as Favorite") {
selectedLandmark?.isFavorite.toggle()
}
.disabled(selectedLandmark == nil)
}
}
}

CommandMenu("Landmark") {
Button("\(selectedLandmark?.isFavorite == true ? "Remove" : "Mark") as Favorite") {
selectedLandmark?.isFavorite.toggle()
}
.disabled(selectedLandmark == nil)
}
}

Add a keyboard shortcut for the menu item with the `keyboardShortcut(_:modifiers:)` modifier.

SwiftUI automatically shows the keyboard shortcut in the menu.

CommandMenu("Landmark") {
Button("\(selectedLandmark?.isFavorite == true ? "Remove" : "Mark") as Favorite") {
selectedLandmark?.isFavorite.toggle()
}
.keyboardShortcut("f", modifiers: [.shift, .option])
.disabled(selectedLandmark == nil)
}
}
}

selectedLandmark?.isFavorite.toggle()
}
.keyboardShortcut("f", modifiers: [.shift, .option])
.disabled(selectedLandmark == nil)
}

The menu now contains your new command, but you need to set the `selectedLandmark` focused binding for it to work.

In `LandmarkList`, add a state variable for the selected landmark and a computed property that indicates the index of the selected landmark.

struct LandmarkList: View {
@Environment(ModelData.self) var modelData
@State private var showFavoritesOnly = false
@State private var filter = FilterCategory.all
@State private var selectedLandmark: Landmark?

var index: Int? {
modelData.landmarks.firstIndex(where: { $0.id == selectedLandmark?.id })
}

#Preview {

@State private var showFavoritesOnly = false
@State private var filter = FilterCategory.all
@State private var selectedLandmark: Landmark?

Initialize the `List` with a binding to the selected value, and add a tag to the navigation link.

The tag associates a particular landmark with the given item in the `ForEach`, which then drives the selection.

var body: some View {
NavigationSplitView {
List(selection: $selectedLandmark) {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
.tag(landmark)
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle(title)
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {
Picker("Category", selection: $filter) {
ForEach(FilterCategory.allCases) { category in
Text(category.rawValue).tag(category)
}
}
.pickerStyle(.inline)

#Preview {

var body: some View {
NavigationSplitView {
List(selection: $selectedLandmark) {
ForEach(filteredLandmarks) { landmark in
NavigationLink {

Add the `focusedValue(_:_:)` modifier to the `NavigationSplitView`, providing a binding the value from the `landmarks` array.

You perform a look-up here to ensure that you are modifying the landmark stored in the model, and not a copy.

NavigationSplitView {
List(selection: $selectedLandmark) {
ForEach(filteredLandmarks) { landmark in
NavigationLink {
LandmarkDetail(landmark: landmark)
} label: {
LandmarkRow(landmark: landmark)
}
.tag(landmark)
}
}
.animation(.default, value: filteredLandmarks)
.navigationTitle(title)
.frame(minWidth: 300)
.toolbar {
ToolbarItem {
Menu {
Picker("Category", selection: $filter) {
ForEach(FilterCategory.allCases) { category in
Text(category.rawValue).tag(category)
}
}
.pickerStyle(.inline)

Toggle(isOn: $showFavoritesOnly) {
Label("Favorites only", systemImage: "star.fill")
}
} label: {
Label("Filter", systemImage: "slider.horizontal.3")
}
}
}
} detail: {
Text("Select a Landmark")
}
.focusedValue(\.selectedLandmark, $modelData.landmarks[index ?? 0])
}
}

#Preview {

NavigationSplitView {
List(selection: $selectedLandmark) {

Run the macOS app and try out the new menu item.

Content description: A video showing the selection of the Landmark menu item being used to set a landmark as a favorite.

Section 7

## Add preferences with a settings scene

Users expect to be able to adjust settings for a macOS app using the standard Settings menu item. You’ll add preferences to MacLandmarks by adding a `Settings` scene. The scene’s views define the contents of the preferences window, which you’ll use to control the initial zoom level of the `MapView`. You communicate the value to the map view, and store it persistently, by using the `@AppStorage` property wrapper.

You’ll start by adding a control in the `MapView` that sets the initial zoom to one of three levels: near, medium, or far.

In `MapView`, add a `Zoom` enumeration to characterize the zoom level.

MapView.swift

struct MapView: View {
var coordinate: CLLocationCoordinate2D

enum Zoom: String, CaseIterable, Identifiable {
case near = "Near"
case medium = "Medium"
case far = "Far"

var id: Zoom {
return self
}
}

var body: some View {
Map(initialPosition: .region(region))
}

private var region: MKCoordinateRegion {
MKCoordinateRegion(
center: coordinate,
span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
)
}
}

#Preview {
MapView(coordinate: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868))
}

var coordinate: CLLocationCoordinate2D

var id: Zoom {

Add an `@AppStorage` property called `zoom` that takes on the `medium` zoom level by default.

Use a storage key that uniquely identifies the parameter like you would when storing items in `UserDefaults`, because that’s the underlying mechanism that SwiftUI relies on.

@AppStorage("MapView.zoom")
private var zoom: Zoom = .medium

#Preview {

enum Zoom: String, CaseIterable, Identifiable {
case near = "Near"

Change the longitude and latitude delta used to construct the `region` property to a value that depends on `zoom`.

var delta: CLLocationDegrees {
switch zoom {
case .near: return 0.02
case .medium: return 0.2
case .far: return 2
}
}

private var region: MKCoordinateRegion {
MKCoordinateRegion(
center: coordinate,
span: MKCoordinateSpan(latitudeDelta: delta, longitudeDelta: delta)
)
}
}

#Preview {

var body: some View {
Map(initialPosition: .region(region))

Next, you’ll create a `Settings` scene that controls the stored `zoom` value.

Create a new SwiftUI view called `LandmarkSettings` that targets only the macOS app.

LandmarkSettings.swift

struct LandmarkSettings: View {
var body: some View {
Text("Hello, World!")
}
}

#Preview {
LandmarkSettings()
}

#Preview {

Add an `@AppStorage` property that uses the same key as you used in the map view.

struct LandmarkSettings: View {
@AppStorage("MapView.zoom")
private var zoom: MapView.Zoom = .medium

var body: some View {
Text("Hello, World!")
}
}

#Preview {

var body: some View {
Text("Hello, World!")

Add a `Picker` that controls the `zoom` value through a binding.

You typically use a `Form` to arrange controls in your settings view.

var body: some View {
Form {
Picker("Map Zoom:", selection: $zoom) {
ForEach(MapView.Zoom.allCases) { level in
Text(level.rawValue)
}
}
.pickerStyle(.inline)
}
.frame(width: 300)
.navigationTitle("Landmark Settings")
.padding(80)
}
}

#Preview {

In `LandmarksApp`, add the `Settings` scene to your app, but only for macOS.

#if !os(watchOS)

#if os(watchOS)

#if os(macOS)
Settings {
LandmarkSettings()
}
#endif

#if os(macOS)
#endif
Settings {
LandmarkSettings()
}
}
}

Run the app and try changing the settings.

Notice that the map refreshes whenever you change the zoom level.

Content description: A screen recording showing the selection of the MacLandmarks settings menu item.

#Preview {

## Check Your Understanding

Question 1 of 4

Why does the Landmarks app define the `filteredLandmarks` array in a view instead of inside the model?

Possible answers

The model can’t access the filter settings.

You shouldn’t put computed properties in your model.

So the app can easily present different filtered lists in different windows.

Submit Next question

---

