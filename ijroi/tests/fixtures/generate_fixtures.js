// run like /System/Library/Frameworks/JavaVM.framework/Commands/java -jar /Applications/Fiji.app/jars/ij-1.49q.jar -batch generate_fixtures.js

importClass(Packages.ij.gui.Roi);
importClass(Packages.ij.gui.PolygonRoi);
importClass(Packages.ij.IJ);
importClass(Packages.ij.ImagePlus);
importClass(Packages.ij.io.RoiEncoder);
importClass(Packages.ij.process.ByteProcessor);

var processor = ByteProcessor(100, 100);
var imp = ImagePlus("ImagePlus", processor);

var unit_rectangle = Roi(0, 0, 1, 1);
RoiEncoder.save(unit_rectangle, "unit_rectangle.roi");

var x = new java.lang.reflect.Array.newInstance(java.lang.Float.TYPE, 100);
var y = new java.lang.reflect.Array.newInstance(java.lang.Float.TYPE, 100);

for(var i = 0; i < 100; ++i) {
	x[i] = 10 + Math.cos(i/100.0 * 2*Math.PI);
	y[i] = 10 + Math.sin(i/100.0 * 2*Math.PI);
}

freehand_circle = PolygonRoi(x, y, 100, Roi.FREEROI);
RoiEncoder.save(freehand_circle, "freehand_circle.roi");

"Success";