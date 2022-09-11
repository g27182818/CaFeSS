<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="10" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="26" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes"/>
<layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="con-molex" urn="urn:adsk.eagle:library:165">
<description>&lt;b&gt;Molex Connectors&lt;/b&gt;&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="22-23-2031" urn="urn:adsk.eagle:footprint:8078260/1" library_version="5">
<description>&lt;b&gt;KK® 254 Solid Header, Vertical, with Friction Lock, 3 Circuits, Tin (Sn) Plating&lt;/b&gt;&lt;p&gt;&lt;a href =http://www.molex.com/pdm_docs/sd/022232031_sd.pdf&gt;Datasheet &lt;/a&gt;</description>
<wire x1="-3.81" y1="3.175" x2="3.81" y2="3.175" width="0.254" layer="21"/>
<wire x1="3.81" y1="3.175" x2="3.81" y2="1.27" width="0.254" layer="21"/>
<wire x1="3.81" y1="1.27" x2="3.81" y2="-3.175" width="0.254" layer="21"/>
<wire x1="3.81" y1="-3.175" x2="-3.81" y2="-3.175" width="0.254" layer="21"/>
<wire x1="-3.81" y1="-3.175" x2="-3.81" y2="1.27" width="0.254" layer="21"/>
<wire x1="-3.81" y1="1.27" x2="-3.81" y2="3.175" width="0.254" layer="21"/>
<wire x1="-3.81" y1="1.27" x2="3.81" y2="1.27" width="0.254" layer="21"/>
<pad name="1" x="-2.54" y="0" drill="1" shape="long" rot="R90"/>
<pad name="2" x="0" y="0" drill="1" shape="long" rot="R90"/>
<pad name="3" x="2.54" y="0" drill="1" shape="long" rot="R90"/>
<text x="-3.81" y="3.81" size="1.016" layer="25" ratio="10">&gt;NAME</text>
<text x="-3.81" y="-5.08" size="1.016" layer="27" ratio="10">&gt;VALUE</text>
</package>
</packages>
<packages3d>
<package3d name="22-23-2031" urn="urn:adsk.eagle:package:8078634/1" type="box" library_version="5">
<description>&lt;b&gt;KK® 254 Solid Header, Vertical, with Friction Lock, 3 Circuits, Tin (Sn) Plating&lt;/b&gt;&lt;p&gt;&lt;a href =http://www.molex.com/pdm_docs/sd/022232031_sd.pdf&gt;Datasheet &lt;/a&gt;</description>
<packageinstances>
<packageinstance name="22-23-2031"/>
</packageinstances>
</package3d>
</packages3d>
<symbols>
<symbol name="MV" urn="urn:adsk.eagle:symbol:6783/2" library_version="5">
<wire x1="1.27" y1="0" x2="0" y2="0" width="0.6096" layer="94"/>
<text x="2.54" y="-0.762" size="1.524" layer="95">&gt;NAME</text>
<text x="-0.762" y="1.397" size="1.778" layer="96">&gt;VALUE</text>
<pin name="S" x="-2.54" y="0" visible="off" length="short" direction="pas"/>
</symbol>
<symbol name="M" urn="urn:adsk.eagle:symbol:6785/2" library_version="5">
<wire x1="1.27" y1="0" x2="0" y2="0" width="0.6096" layer="94"/>
<text x="2.54" y="-0.762" size="1.524" layer="95">&gt;NAME</text>
<pin name="S" x="-2.54" y="0" visible="off" length="short" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="22-23-2031" urn="urn:adsk.eagle:component:8078937/3" prefix="X" library_version="5">
<description>.100" (2.54mm) Center Header - 3 Pin</description>
<gates>
<gate name="-1" symbol="MV" x="0" y="2.54" addlevel="always" swaplevel="1"/>
<gate name="-2" symbol="M" x="0" y="0" addlevel="always" swaplevel="1"/>
<gate name="-3" symbol="M" x="0" y="-2.54" addlevel="always" swaplevel="1"/>
</gates>
<devices>
<device name="" package="22-23-2031">
<connects>
<connect gate="-1" pin="S" pad="1"/>
<connect gate="-2" pin="S" pad="2"/>
<connect gate="-3" pin="S" pad="3"/>
</connects>
<package3dinstances>
<package3dinstance package3d_urn="urn:adsk.eagle:package:8078634/1"/>
</package3dinstances>
<technologies>
<technology name="">
<attribute name="MF" value="MOLEX" constant="no"/>
<attribute name="MPN" value="22-23-2031" constant="no"/>
<attribute name="OC_FARNELL" value="1462950" constant="no"/>
<attribute name="OC_NEWARK" value="30C0862" constant="no"/>
<attribute name="POPULARITY" value="35" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="USB_A_TH">
<packages>
<package name="CONN4_292303_TEC">
<pad name="1" x="0" y="0" drill="0.9906" diameter="1.4986"/>
<pad name="2" x="2.4892" y="0" drill="0.9906" diameter="1.4986"/>
<pad name="3" x="4.4958" y="0" drill="0.9906" diameter="1.4986"/>
<pad name="4" x="7.0104" y="0" drill="0.9906" diameter="1.4986"/>
<pad name="5" x="-3.0734" y="-2.7178" drill="2.3114" diameter="2.8194"/>
<pad name="6" x="10.0584" y="-2.7178" drill="2.3114" diameter="2.8194"/>
<wire x1="-3.2004" y1="-13.1064" x2="10.1854" y2="-13.1064" width="0.1524" layer="21"/>
<wire x1="10.1854" y1="-13.1064" x2="10.1854" y2="-4.445" width="0.1524" layer="21"/>
<wire x1="10.1854" y1="1.143" x2="-3.2004" y2="1.143" width="0.1524" layer="21"/>
<wire x1="-3.2004" y1="1.143" x2="-3.2004" y2="-0.9652" width="0.1524" layer="21"/>
<wire x1="-3.2004" y1="-4.445" x2="-3.2004" y2="-13.1064" width="0.1524" layer="21"/>
<wire x1="10.1854" y1="-0.9652" x2="10.1854" y2="1.143" width="0.1524" layer="21"/>
<wire x1="0.381" y1="2.54" x2="-0.381" y2="2.54" width="0.508" layer="21" curve="-180"/>
<wire x1="-0.381" y1="2.54" x2="0.381" y2="2.54" width="0.508" layer="21" curve="-180"/>
<wire x1="-3.0734" y1="-12.9794" x2="10.0584" y2="-12.9794" width="0.1524" layer="51"/>
<wire x1="10.0584" y1="-12.9794" x2="10.0584" y2="1.016" width="0.1524" layer="51"/>
<wire x1="10.0584" y1="1.016" x2="-3.0734" y2="1.016" width="0.1524" layer="51"/>
<wire x1="-3.0734" y1="1.016" x2="-3.0734" y2="-12.9794" width="0.1524" layer="51"/>
<wire x1="0.381" y1="-1.905" x2="-0.381" y2="-1.905" width="0.508" layer="51" curve="-180"/>
<wire x1="-0.381" y1="-1.905" x2="0.381" y2="-1.905" width="0.508" layer="51" curve="-180"/>
<wire x1="0.381" y1="2.54" x2="-0.381" y2="2.54" width="0.508" layer="22" curve="-180"/>
<wire x1="-0.381" y1="2.54" x2="0.381" y2="2.54" width="0.508" layer="22" curve="-180"/>
<text x="0.2286" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;Name</text>
<text x="1.778" y="-0.635" size="1.27" layer="27" ratio="6" rot="SR0">&gt;Value</text>
</package>
</packages>
<symbols>
<symbol name="CONN4_292303">
<pin name="1" x="0" y="0" visible="pad" length="middle" direction="pas"/>
<pin name="2" x="0" y="-2.54" visible="pad" length="middle" direction="pas"/>
<pin name="3" x="0" y="-5.08" visible="pad" length="middle" direction="pas"/>
<pin name="4" x="0" y="-7.62" visible="pad" length="middle" direction="pas"/>
<pin name="5" x="0" y="-10.16" visible="pad" length="middle" direction="pas"/>
<pin name="6" x="0" y="-12.7" visible="pad" length="middle" direction="pas"/>
<wire x1="5.08" y1="2.54" x2="5.08" y2="-15.24" width="0.1524" layer="94"/>
<wire x1="5.08" y1="-15.24" x2="15.24" y2="-15.24" width="0.1524" layer="94"/>
<wire x1="17.78" y1="-12.7" x2="17.78" y2="0" width="0.1524" layer="94"/>
<wire x1="15.24" y1="2.54" x2="5.08" y2="2.54" width="0.1524" layer="94"/>
<wire x1="12.065" y1="-2.8448" x2="12.065" y2="-3.5052" width="0.1524" layer="94"/>
<wire x1="12.065" y1="-3.5052" x2="12.7" y2="-3.5052" width="0.1524" layer="94"/>
<wire x1="12.7" y1="-3.5052" x2="12.7" y2="-2.8448" width="0.1524" layer="94"/>
<wire x1="12.7" y1="-2.8448" x2="12.065" y2="-2.8448" width="0.1524" layer="94"/>
<wire x1="14.605" y1="-1.27" x2="14.605" y2="-3.81" width="0.1524" layer="94"/>
<wire x1="14.605" y1="-3.81" x2="14.605" y2="-5.08" width="0.1524" layer="94"/>
<wire x1="14.605" y1="-5.08" x2="14.605" y2="-6.985" width="0.1524" layer="94"/>
<wire x1="12.3952" y1="-3.175" x2="12.3952" y2="-3.81" width="0.1524" layer="94"/>
<wire x1="12.3952" y1="-3.81" x2="14.605" y2="-5.08" width="0.1524" layer="94"/>
<wire x1="16.8148" y1="-2.54" x2="16.8148" y2="-2.8448" width="0.1524" layer="94"/>
<wire x1="16.8148" y1="-2.8448" x2="14.605" y2="-3.81" width="0.1524" layer="94"/>
<wire x1="13.6652" y1="-1.27" x2="15.5448" y2="-1.27" width="0.1524" layer="94"/>
<wire x1="14.605" y1="0" x2="13.6652" y2="-1.27" width="0.1524" layer="94"/>
<wire x1="14.605" y1="0" x2="15.5448" y2="-1.27" width="0.1524" layer="94"/>
<wire x1="15.24" y1="2.54" x2="17.78" y2="0" width="0.1524" layer="94"/>
<wire x1="17.78" y1="-12.7" x2="15.24" y2="-15.24" width="0.1524" layer="94"/>
<wire x1="15.24" y1="-6.985" x2="13.97" y2="-6.985" width="0.127" layer="94" curve="-180"/>
<wire x1="13.97" y1="-6.985" x2="15.24" y2="-6.985" width="0.127" layer="94" curve="-180"/>
<wire x1="17.1196" y1="-2.2352" x2="16.51" y2="-2.2352" width="0.127" layer="94" curve="-180"/>
<wire x1="16.51" y1="-2.2352" x2="17.1196" y2="-2.2098" width="0.127" layer="94" curve="-180"/>
<polygon width="0.0254" layer="94">
<vertex x="14.605" y="0"/>
<vertex x="13.6525" y="-1.27"/>
<vertex x="15.5575" y="-1.27"/>
</polygon>
<text x="4.1656" y="5.3086" size="2.0828" layer="95" ratio="6" rot="SR0">&gt;Name</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="292303-3" prefix="J">
<gates>
<gate name="A" symbol="CONN4_292303" x="0" y="0"/>
</gates>
<devices>
<device name="" package="CONN4_292303_TEC">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
<connect gate="A" pin="4" pad="4"/>
<connect gate="A" pin="5" pad="5"/>
<connect gate="A" pin="6" pad="6"/>
</connects>
<technologies>
<technology name="">
<attribute name="BUILT_BY" value="EMA_UL_Team" constant="no"/>
<attribute name="COPYRIGHT" value="Copyright (C) 2016 Accelerated Designs. All rights reserved" constant="no"/>
<attribute name="DESCRIPTION" value="USB A R/A RCPT ASSY THRU HOLE, LEAD FREE" constant="no"/>
<attribute name="MANUFACTURER_PART_NUMBER" value="292303-3" constant="no"/>
<attribute name="PITCH_MM_" value="2.5" constant="no"/>
<attribute name="POSITIONS" value="4" constant="no"/>
<attribute name="PRODUCT" value="Connector" constant="no"/>
<attribute name="ROWS-CONFIG" value="1" constant="no"/>
<attribute name="SOURCELIBRARY" value="TE_Connectivity-2018-03-16" constant="no"/>
<attribute name="TE_PART_NUMBER" value="292303-3" constant="no"/>
<attribute name="TYPE" value="USB 2.0" constant="no"/>
<attribute name="VENDOR" value="TE Connectivity" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="S0" library="con-molex" library_urn="urn:adsk.eagle:library:165" deviceset="22-23-2031" device="" package3d_urn="urn:adsk.eagle:package:8078634/1" override_package3d_urn="urn:adsk.eagle:package:29594896/2" override_package_urn="urn:adsk.eagle:footprint:8078260/1"/>
<part name="S1" library="con-molex" library_urn="urn:adsk.eagle:library:165" deviceset="22-23-2031" device="" package3d_urn="urn:adsk.eagle:package:8078634/1" override_package3d_urn="urn:adsk.eagle:package:29594942/2" override_package_urn="urn:adsk.eagle:footprint:8078260/1"/>
<part name="S2" library="con-molex" library_urn="urn:adsk.eagle:library:165" deviceset="22-23-2031" device="" package3d_urn="urn:adsk.eagle:package:8078634/1" override_package3d_urn="urn:adsk.eagle:package:29594947/2" override_package_urn="urn:adsk.eagle:footprint:8078260/1"/>
<part name="J1" library="USB_A_TH" deviceset="292303-3" device="" override_package3d_urn="urn:adsk.eagle:package:29594893/3" override_package_urn="urn:adsk.eagle:footprint:29594894/1"/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="S0" gate="-1" x="7.62" y="60.96" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="61.722" size="1.524" layer="95" rot="R180"/>
<attribute name="VALUE" x="8.382" y="59.563" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="S0" gate="-2" x="7.62" y="63.5" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="64.262" size="1.524" layer="95" rot="R180"/>
</instance>
<instance part="S0" gate="-3" x="7.62" y="66.04" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="66.802" size="1.524" layer="95" rot="R180"/>
</instance>
<instance part="S1" gate="-1" x="7.62" y="48.26" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="49.022" size="1.524" layer="95" rot="R180"/>
<attribute name="VALUE" x="8.382" y="46.863" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="S1" gate="-2" x="7.62" y="50.8" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="51.562" size="1.524" layer="95" rot="R180"/>
</instance>
<instance part="S1" gate="-3" x="7.62" y="53.34" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="54.102" size="1.524" layer="95" rot="R180"/>
</instance>
<instance part="S2" gate="-1" x="7.62" y="35.56" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="36.322" size="1.524" layer="95" rot="R180"/>
<attribute name="VALUE" x="8.382" y="34.163" size="1.778" layer="96" rot="R180"/>
</instance>
<instance part="S2" gate="-2" x="7.62" y="38.1" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="38.862" size="1.524" layer="95" rot="R180"/>
</instance>
<instance part="S2" gate="-3" x="7.62" y="40.64" smashed="yes" rot="R180">
<attribute name="NAME" x="5.08" y="41.402" size="1.524" layer="95" rot="R180"/>
</instance>
<instance part="J1" gate="A" x="43.18" y="58.42" smashed="yes">
<attribute name="NAME" x="47.3456" y="63.7286" size="2.0828" layer="95" ratio="6" rot="SR0"/>
</instance>
</instances>
<busses>
</busses>
<nets>
<net name="D" class="0">
<segment>
<pinref part="S0" gate="-1" pin="S"/>
<wire x1="10.16" y1="60.96" x2="20.32" y2="60.96" width="0.1524" layer="91"/>
<label x="12.7" y="60.96" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="S1" gate="-1" pin="S"/>
<wire x1="10.16" y1="48.26" x2="20.32" y2="48.26" width="0.1524" layer="91"/>
<label x="12.7" y="48.26" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="S2" gate="-1" pin="S"/>
<wire x1="10.16" y1="35.56" x2="20.32" y2="35.56" width="0.1524" layer="91"/>
<label x="12.7" y="35.56" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="J1" gate="A" pin="3"/>
<wire x1="43.18" y1="53.34" x2="35.56" y2="53.34" width="0.1524" layer="91"/>
<label x="35.56" y="53.34" size="1.778" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="S0" gate="-3" pin="S"/>
<wire x1="10.16" y1="66.04" x2="20.32" y2="66.04" width="0.1524" layer="91"/>
<label x="12.7" y="66.04" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="S1" gate="-3" pin="S"/>
<wire x1="10.16" y1="53.34" x2="20.32" y2="53.34" width="0.1524" layer="91"/>
<label x="12.7" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="S2" gate="-3" pin="S"/>
<wire x1="10.16" y1="40.64" x2="20.32" y2="40.64" width="0.1524" layer="91"/>
<label x="12.7" y="40.64" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="J1" gate="A" pin="5"/>
<wire x1="43.18" y1="48.26" x2="35.56" y2="48.26" width="0.1524" layer="91"/>
<label x="35.56" y="48.26" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="J1" gate="A" pin="6"/>
<wire x1="43.18" y1="45.72" x2="35.56" y2="45.72" width="0.1524" layer="91"/>
<label x="35.56" y="45.72" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="J1" gate="A" pin="1"/>
<wire x1="43.18" y1="58.42" x2="35.56" y2="58.42" width="0.1524" layer="91"/>
<label x="35.56" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="J1" gate="A" pin="4"/>
<wire x1="43.18" y1="50.8" x2="35.56" y2="50.8" width="0.1524" layer="91"/>
<label x="35.56" y="50.8" size="1.778" layer="95"/>
</segment>
</net>
<net name="5V" class="0">
<segment>
<pinref part="S0" gate="-2" pin="S"/>
<wire x1="10.16" y1="63.5" x2="20.32" y2="63.5" width="0.1524" layer="91"/>
<label x="12.7" y="63.5" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="S1" gate="-2" pin="S"/>
<wire x1="10.16" y1="50.8" x2="20.32" y2="50.8" width="0.1524" layer="91"/>
<label x="12.7" y="50.8" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="S2" gate="-2" pin="S"/>
<wire x1="10.16" y1="38.1" x2="20.32" y2="38.1" width="0.1524" layer="91"/>
<label x="12.7" y="38.1" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="J1" gate="A" pin="2"/>
<wire x1="43.18" y1="55.88" x2="35.56" y2="55.88" width="0.1524" layer="91"/>
<label x="35.56" y="55.88" size="1.778" layer="95"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
<compatibility>
<note version="8.2" severity="warning">
Since Version 8.2, EAGLE supports online libraries. The ids
of those online libraries will not be understood (or retained)
with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports URNs for individual library
assets (packages, symbols, and devices). The URNs of those assets
will not be understood (or retained) with this version.
</note>
<note version="8.3" severity="warning">
Since Version 8.3, EAGLE supports the association of 3D packages
with devices in libraries, schematics, and board files. Those 3D
packages will not be understood (or retained) with this version.
</note>
<note version="9.4" severity="warning">
Since Version 9.4, EAGLE supports the overriding of 3D packages
in schematics and board files. Those overridden 3d packages
will not be understood (or retained) with this version.
</note>
</compatibility>
</eagle>
