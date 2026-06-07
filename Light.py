import math
import altair as alt
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Light - Class 10 Science", layout="wide")
st.title("Light")
st.subheader("A website that provides extremely detailed information about the Light chapter for Class 10 science.")
st.write("Use the sidebar to choose a topic, then click `Get INFO` to see a deep explanation, key formulas, examples, and diagrams.")


def draw_reflection_diagram(angle):
    theta = math.radians(angle)
    incident = pd.DataFrame([
        {"x": -math.sin(theta), "y": math.cos(theta)},
        {"x": 0.0, "y": 0.0},
    ])
    reflected = pd.DataFrame([
        {"x": 0.0, "y": 0.0},
        {"x": math.sin(theta), "y": math.cos(theta)},
    ])
    normal = pd.DataFrame([
        {"x": 0.0, "y": 0.0},
        {"x": 0.0, "y": 1.2},
    ])
    mirror = pd.DataFrame([
        {"x": -1.0, "y": 0.0},
        {"x": 1.0, "y": 0.0},
    ])
    labels = pd.DataFrame([
        {"x": 0.05, "y": 0.40, "text": f"θ_i = θ_r = {angle}°"},
    ])
    chart = alt.Chart(incident).mark_line(color="#1f77b4", strokeWidth=4).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(reflected).mark_line(color="#2ca02c", strokeWidth=4).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(normal).mark_line(color="gray", strokeDash=[5, 5], strokeWidth=2).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(mirror).mark_line(color="black", strokeWidth=5).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(labels).mark_text(align="left", dx=5, dy=-5, fontSize=14).encode(x="x:Q", y="y:Q", text="text:N")
    return chart.properties(width=500, height=350).configure_axis(grid=False, labels=False, domain=False, ticks=False).configure_view(strokeWidth=0)


def draw_refraction_diagram(incident, n1, n2):
    theta = math.radians(incident)
    sin_r = n1 * math.sin(theta) / n2
    if sin_r > 1:
        return None
    refracted = math.asin(sin_r)
    incident_ray = pd.DataFrame([
        {"x": -math.sin(theta), "y": math.cos(theta)},
        {"x": 0.0, "y": 0.0},
    ])
    refracted_ray = pd.DataFrame([
        {"x": 0.0, "y": 0.0},
        {"x": math.sin(refracted), "y": -math.cos(refracted)},
    ])
    normal = pd.DataFrame([
        {"x": 0.0, "y": 1.2},
        {"x": 0.0, "y": -1.2},
    ])
    boundary = pd.DataFrame([
        {"x": -1.0, "y": 0.0},
        {"x": 1.0, "y": 0.0},
    ])
    labels = pd.DataFrame([
        {"x": 0.05, "y": 0.40, "text": f"θ_i = {incident}°"},
        {"x": 0.05, "y": -0.35, "text": f"θ_r = {math.degrees(refracted):.1f}°"},
    ])
    chart = alt.Chart(incident_ray).mark_line(color="#1f77b4", strokeWidth=4).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(refracted_ray).mark_line(color="#d62728", strokeWidth=4).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(normal).mark_line(color="gray", strokeDash=[5, 5], strokeWidth=2).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(boundary).mark_line(color="black", strokeWidth=5).encode(x="x:Q", y="y:Q")
    chart += alt.Chart(labels).mark_text(align="left", dx=5, fontSize=14).encode(x="x:Q", y="y:Q", text="text:N")
    return chart.properties(width=500, height=350).configure_axis(grid=False, labels=False, domain=False, ticks=False).configure_view(strokeWidth=0)

# Initialize session state
if "show_info" not in st.session_state:
    st.session_state.show_info = False
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = "Reflection of Light"
if "selected_info" not in st.session_state:
    st.session_state.selected_info = []

sidebar = st.sidebar
sidebar.header("Topic selector")
topics = [
    "Reflection of Light",
    "Refraction of Light",
    "Formation of Image by a Plane Mirror",
    "Laws of Reflection",
    "Types of Reflection",
    "Spherical Mirrors",
    "Laws of Refraction",
    "Magnification and Mirror Formula",
    "Lenses",
]

topic = sidebar.selectbox("Choose a topic", topics, index=topics.index(st.session_state.selected_topic))
additional_info = sidebar.multiselect(
    "Additional details to include",
    ["Examples", "Diagrams", "Real-life applications", "Historical background", "Visualize It"],
    default=st.session_state.selected_info,
)

if sidebar.button("Get INFO"):
    st.session_state.show_info = True
    st.session_state.selected_topic = topic
    st.session_state.selected_info = additional_info

sidebar.write("### How to use")
sidebar.write("1. Select a topic above.\n2. Choose any optional details.\n3. Click `Get INFO` to display the detailed content and formulas.")


def get_topic_content(topic_name):
    if topic_name == "Reflection of Light":
        sections = [
            {
                "heading": "What is reflection of light?",
                "text": (
                    "Reflection of light is the process by which a light ray bounces back when it strikes a smooth surface. "
                    "The reflected ray stays in the same medium as the incident ray, and the surface acts like a mirror. "
                    "This is the basic principle behind mirrors, shiny objects, and optical instruments."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "A ray of light incident on a surface makes an angle with the normal at the point of incidence. "
                    "According to the law of reflection, the angle of reflection is equal to the angle of incidence, and the incident ray, reflected ray, and normal all lie in the same plane. "
                    "This principle is valid for smooth, polished surfaces called plane mirrors."
                ),
            },
            {
                "heading": "Key formulas and concepts",
                "text": (
                    "- Angle of incidence (i) = Angle of reflection (r).\n"
                    "- Plane mirrors produce virtual images that are laterally inverted.\n"
                    "- The image distance from the mirror is equal to the object distance.\n"
                    "- The size of the image in a plane mirror is the same as the object size."
                ),
            },
        ]
        
        extra = {
            "Examples": (
                "A car headlight beam reflecting from a polished road surface, or a person looking at themselves in a mirror, show how reflected rays obey the reflection law. "
                "The uniform reflection of a laser beam from a mirror is a clear example of regular reflection."
            ),
            "Diagrams": (
                "The best diagram is a ray diagram showing the incident ray, reflected ray, normal, and angles i and r. "
                "In a plane mirror, the image appears to lie behind the mirror at the same distance as the object."
            ),
            "Real-life applications": (
                "Reflecting telescopes, periscopes, rearview mirrors, and safety reflectors all use reflection of light. "
                "Architects also use reflective surfaces to direct natural light in buildings."
            ),
            "Historical background": (
                "The basic law of reflection was known to ancient Greek mathematicians and was described in Euclid's Optics. "
                "Modern mathematical formulation emerged in the 17th century as part of geometric optics."
            ),
            "Visualize It": (
                "Use the interactive lab below to explore how the angle of incidence and angle of reflection stay equal, and see the reflection law in action."
            ),
        }
        return sections, [], extra

    if topic_name == "Refraction of Light":
        sections = [
            {
                "heading": "What is refraction of light?",
                "text": (
                    "Refraction is the bending of light as it passes from one transparent medium into another, because the speed of light changes. "
                    "This change of direction occurs at the boundary between media such as air, water, or glass."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "When a light ray enters a denser medium, it slows down and bends toward the normal. When it enters a rarer medium, it speeds up and bends away from the normal. "
                    "The amount of bending depends on the refractive indices of the two media and the angle of incidence."
                ),
            },
            {
                "heading": "Key formulas and concepts",
                "text": (
                    "- Snell's law: n1 * sin(i) = n2 * sin(r).\n"
                    "- Refractive index of a medium is the ratio of the speed of light in vacuum to speed in that medium.\n"
                    "- The refracted ray, incident ray, and normal all lie in the same plane."
                ),
            },
        ]
       
        extra = {
            "Examples": (
                "A straw appearing bent in a glass of water, or the apparent shift of a coin lying at the bottom of a bowl, are everyday examples of refraction."
            ),
            "Diagrams": (
                "Ray diagrams for refraction show the incident ray, refracted ray, normal, and the change of direction at the boundary."
            ),
            "Real-life applications": (
                "Lenses in glasses, cameras, microscopes, and telescopes work by refracting light to focus images. "
                "Optical fibers use controlled refraction to transmit light over long distances."
            ),
            "Historical background": (
                "Willebrord Snellius formulated Snell's law in the early 17th century, and René Descartes independently described the law using mathematical optics."
            ),
            "Visualize It": (
                "Use the interactive lab below to change the incident angle and refractive indices, then observe how the refracted angle is calculated from Snell's law."
            ),
        }
        return sections, [], extra

    if topic_name == "Formation of Image by a Plane Mirror":
        sections = [
            {
                "heading": "How a plane mirror forms an image",
                "text": (
                    "A plane mirror creates a virtual image that appears to be the same distance behind the mirror as the object is in front of it. "
                    "The rays diverge after reflection, but appear to come from a point behind the mirror."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "The image is virtual because light rays do not actually converge at the image point; the image can only be seen, not captured on a screen. "
                    "The image is erect, of the same size as the object, and laterally inverted."
                ),
            },
            {
                "heading": "Key properties",
                "text": (
                    "- Image distance = object distance.\n"
                    "- Image size = object size.\n"
                    "- The image is virtual and erect.\n"
                    "- Lateral inversion means left and right are swapped."
                ),
            },
        ]
      
        extra = {
            "Examples": (
                "A person seeing their reflection in a mirror, dressing mirrors, and bathroom cabinets are classic examples."
            ),
            "Diagrams": (
                "Ray diagrams for plane mirrors use two incident rays from the object: one parallel to the mirror surface and one towards the normal."
            ),
            "Real-life applications": (
                "Security mirrors, periscopes, and optical instruments use plane mirror image formation."
            ),
            "Historical background": (
                "The optical behavior of plane mirrors was studied in ancient times and formalized in mathematical optics by medieval and Renaissance scholars."
            ),
            "Visualize It": (
                "This interactive lab lets you compare object and image distances for a plane mirror and see why the image appears behind the mirror."
            ),
        }
        return sections, [], extra

    if topic_name == "Laws of Reflection":
        sections = [
            {
                "heading": "Laws of reflection",
                "text": (
                    "There are two fundamental laws of reflection: (1) the incident ray, reflected ray, and normal lie in the same plane; "
                    "(2) the angle of incidence is equal to the angle of reflection."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "These laws are exact for smooth, polished surfaces. They are the basis for predicting the direction of reflected rays in mirrors and optical devices. "
                    "The laws apply to both regular and irregular reflection, though the latter scatters light in many directions."
                ),
            },
            {
                "heading": "Mathematical expression",
                "text": (
                    "If i is the angle between the incident ray and normal, and r is the angle between the reflected ray and normal, then i = r. "
                    "This relation is independent of the wavelength or color of light."
                ),
            },
        ]
        
        extra = {
            "Examples": (
                "A laser pointer reflected from a mirror follows the same angle pattern every time, demonstrating the law precisely."
            ),
            "Diagrams": (
                "Ray diagrams show the equal angles and how the reflected ray stays in the same plane as the incident ray."
            ),
            "Real-life applications": (
                "Sunlight reflected from calm water or polished metal surfaces follows the laws of reflection."
            ),
            "Historical background": (
                "Euclid and later Ibn al-Haytham documented the geometrical behavior of reflection, laying the groundwork for modern optics."
            ),
            "Visualize It": (
                "Explore reflection angles with an interactive slider and see the same law hold for every smooth surface and mirror."
            ),
        }
        return sections, [], extra

    if topic_name == "Types of Reflection":
        sections = [
            {
                "heading": "Regular and diffuse reflection",
                "text": (
                    "There are two main types of reflection: regular reflection from smooth surfaces and diffuse reflection from rough surfaces. "
                    "Regular reflection preserves the shape of a beam, while diffuse reflection scatters light in many directions."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "A polished mirror reflects rays so that parallel incident rays remain parallel after reflection. A rough surface makes rays strike at different angles, so the reflected rays spread out. "
                    "Diffuse reflection is what allows us to see non-shiny objects from any angle."
                ),
            },
            {
                "heading": "Key distinctions",
                "text": (
                    "- Regular reflection: smooth surface, clear image.\n"
                    "- Diffuse reflection: rough surface, no image.\n"
                    "- Both types obey the same local law of reflection at each point."
                ),
            },
        ]
        charts = []
        extra = {
            "Examples": (
                "A mirror produces a clear reflected image, while a painted wall reflects light diffusely and does not form a mirror image."
            ),
            "Diagrams": (
                "Draw two surfaces: a flat mirror and a rough paper sheet. Show parallel rays reflecting in one direction from the mirror and scattering from the rough surface."
            ),
            "Real-life applications": (
                "Diffuse reflection is essential for lighting rooms evenly, while regular reflection is used in optical systems and mirrors."
            ),
            "Historical background": (
                "The distinction between regular and diffuse reflection became important with the study of light scattering and surface textures in the 19th century."
            ),
            "Visualize It": (
                "Adjust the incoming ray layout and see how smooth and rough surfaces reflect light differently in the interactive lab."
            ),
        }
        return sections, charts, extra

    if topic_name == "Spherical Mirrors":
        sections = [
            {
                "heading": "What are spherical mirrors?",
                "text": (
                    "Spherical mirrors are segments of a spherical surface. They are divided into concave mirrors, which curve inward, and convex mirrors, which curve outward. "
                    "Their focusing properties depend on the radius of curvature and focal length."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "A concave mirror can form real, inverted images or virtual, erect images depending on the object's position relative to the focal point. "
                    "A convex mirror always forms a virtual, erect, and diminished image."
                ),
            },
            {
                "heading": "Key formulas",
                "text": (
                    "- Mirror formula: 1/f = 1/v + 1/u.\n"
                    "- Magnification: m = -v/u.\n"
                    "- For spherical mirrors, f = R/2, where R is the radius of curvature."
                ),
            },
        ]
        charts = []
        extra = {
            "Examples": (
                "Makeup mirrors use concave mirrors to magnify the face, while car side mirrors use convex mirrors to give a wide field of view."
            ),
            "Diagrams": (
                "Ray diagrams for concave and convex mirrors show how rays converge or diverge as they reflect from the spherical surface."
            ),
            "Real-life applications": (
                "Headlights, satellite dishes, shaving mirrors, and solar concentrators all use spherical mirror principles."
            ),
            "Historical background": (
                "Spherical mirrors were studied by ancient astronomers and later used in telescopes by Galileo and Newton."
            ),
            "Visualize It": (
                "Interactively change the object distance and see how concave and convex mirrors form real or virtual images."
            ),
        }
        return sections, charts, extra

    if topic_name == "Laws of Refraction":
        sections = [
            {
                "heading": "Laws of refraction",
                "text": (
                    "The first law states that the incident ray, refracted ray, and normal lie in the same plane. "
                    "The second law, Snell's law, gives the relationship between the angles and refractive indices."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "For a ray crossing from medium 1 into medium 2, the ratio of the sine of the angle of incidence to the sine of the angle of refraction is constant. "
                    "This constant is the refractive index ratio n2/n1."
                ),
            },
            {
                "heading": "Key formula",
                "text": (
                    "Snell's law: n1 sin(i) = n2 sin(r).\n"
                    "This law explains why prisms split white light into colors and why lenses bend light to form images."
                ),
            },
        ]
        charts = []
        extra = {
            "Examples": (
                "A prism bending light and creating separation of colors is a vivid demonstration of refraction laws."
            ),
            "Diagrams": (
                "Lens and prism ray diagrams illustrate the bending of rays at the boundary and the dependence on refractive indices."
            ),
            "Real-life applications": (
                "Eye lenses, cameras, microscopes, and corrective glasses all depend on refraction laws."
            ),
            "Historical background": (
                "Snell's law was discovered in the early 1600s and became a cornerstone of geometric optics."
            ),
            "Visualize It": (
                "Use the interactive lab below to explore refraction behavior as you change angles and refractive indices."
            ),
        }
        return sections, charts, extra

    if topic_name == "Magnification and Mirror Formula":
        sections = [
            {
                "heading": "Mirror formula and magnification",
                "text": (
                    "The mirror formula relates the focal length of a mirror to the object distance and image distance. Magnification tells us how much larger or smaller the image is compared to the object."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "For concave mirrors, if the object is beyond the focal length, the image is real and inverted with magnification m = -v/u. "
                    "If the object is between the focal point and the mirror, the image becomes virtual, erect, and enlarged."
                ),
            },
            {
                "heading": "Key equations",
                "text": (
                    "- Mirror formula: 1/f = 1/v + 1/u.\n"
                    "- Linear magnification: m = h_i / h_o = -v / u.\n"
                    "- Sign conventions: a real image has positive v and an inverted image has negative magnification."
                ),
            },
        ]
        charts = []
        extra = {
            "Examples": (
                "Objects placed at different distances from a concave mirror produce images that vary from magnified and virtual to reduced and real."
            ),
            "Diagrams": (
                "Ray diagrams show how the image position shifts as the object distance changes, and how magnification changes accordingly."
            ),
            "Real-life applications": (
                "Dentists and makeup mirrors use magnification from concave mirrors, while reflective telescopes use mirror formulas to focus images."
            ),
            "Historical background": (
                "The mirror formula was systematically studied in the 17th century as part of classical optics."
            ),
            "Visualize It": (
                "Experiment with object distance and focal length to see how the image distance and magnification change."
            ),
        }
        return sections, charts, extra

    if topic_name == "Lenses":
        sections = [
            {
                "heading": "Types of lenses",
                "text": (
                    "Lenses are transparent optical elements with curved surfaces that refract light. Convex lenses converge light rays, while concave lenses diverge them."
                ),
            },
            {
                "heading": "Detailed explanation",
                "text": (
                    "The lens formula 1/f = 1/v - 1/u describes the relationship between object distance, image distance, and focal length for thin lenses. "
                    "Convex lenses can form real inverted images or virtual erect images, while concave lenses always form virtual, erect, and diminished images."
                ),
            },
            {
                "heading": "Key formulas",
                "text": (
                    "- Lens formula: 1/f = 1/v - 1/u.\n"
                    "- Magnification: m = v / u.\n"
                    "- For a convex lens, f is positive; for a concave lens, f is negative."
                ),
            },
        ]
        charts = []
        extra = {
            "Examples": (
                "A magnifying glass, a camera lens, and a microscope lens all use convex lens behavior to focus light."
            ),
            "Diagrams": (
                "Ray diagrams for convex and concave lenses show the principal focus, optical axis, and image formation patterns."
            ),
            "Real-life applications": (
                "Eyeglasses, cameras, microscopes, and contact lenses rely on lens formulas to correct vision and form images."
            ),
            "Historical background": (
                "Lens design has advanced since ancient times, with major progress in the Renaissance and modern optics."
            ),
            "Visualize It": (
                "Move the object distance slider and observe how a convex or concave lens changes the image position and size."
            ),
        }
        return sections, charts, extra

    return [], [], {}


if st.session_state.show_info:
    st.header(f"Detailed overview: {st.session_state.selected_topic}")
    sections, charts, extra_content = get_topic_content(st.session_state.selected_topic)
    for section in sections:
        st.subheader(section["heading"])
        st.write(section["text"])

    if st.session_state.selected_info:
        st.markdown("---")
        st.subheader("Selected additional details")
        for choice in st.session_state.selected_info:
            if choice in extra_content:
                st.markdown(f"**{choice}**")
                st.write(extra_content[choice])

    if "Visualize It" in st.session_state.selected_info:
        st.markdown("---")
        st.subheader("Interactive Lab Experience")
        if st.session_state.selected_topic in ["Reflection of Light", "Laws of Reflection"]:
            angle = st.slider("Incident angle (degrees)", 0, 90, 30)
            st.write(f"When the incident angle is **{angle}°**, the reflected angle is also **{angle}°**.")
            st.write("The incident ray, reflected ray, and normal remain in the same plane, so the law of reflection always holds.")
            st.altair_chart(draw_reflection_diagram(angle), use_container_width=True)
        elif st.session_state.selected_topic in ["Refraction of Light", "Laws of Refraction"]:
            n1 = st.number_input("Refractive index n1", 1.0, 3.0, 1.0, 0.01)
            n2 = st.number_input("Refractive index n2", 1.0, 3.0, 1.33, 0.01)
            incident = st.slider("Angle of incidence (degrees)", 0, 89, 30)
            sin_r = n1 * math.sin(math.radians(incident)) / n2
            if sin_r <= 1:
                refracted = math.degrees(math.asin(sin_r))
                st.write(f"Refracted angle = **{refracted:.1f}°**.")
                st.write("This demonstration shows Snell's law and how a ray bends at the boundary.")
                chart = draw_refraction_diagram(incident, n1, n2)
                if chart is not None:
                    st.altair_chart(chart, use_container_width=True)
            else:
                st.write("Total internal reflection occurs when the angle is too large for the second medium.")
        elif st.session_state.selected_topic == "Formation of Image by a Plane Mirror":
            st.write("A plane mirror produces a virtual image the same distance behind the mirror as the object is in front.")
            distance = st.slider("Object distance from mirror (cm)", 5, 100, 30)
            st.write(f"Image distance = **{distance} cm** behind the mirror, matching the object distance.")
            st.write("Try changing the object distance to see the virtual image move in sync.")
        elif st.session_state.selected_topic in ["Spherical Mirrors", "Magnification and Mirror Formula"]:
            focal = st.slider("Focal length f (cm)", 5, 50, 20)
            object_dist = st.slider("Object distance u (cm)", 5, 100, 40)
            if object_dist != 0:
                image_dist = 1 / (1 / focal - 1 / object_dist) if (1 / focal - 1 / object_dist) != 0 else float('inf')
                magnification = -image_dist / object_dist
                st.write(f"Image distance v ≈ **{image_dist:.1f} cm**")
                st.write(f"Magnification m ≈ **{magnification:.2f}**")
                st.write("This interactive model helps you see how mirror formula values change with object position.")
            else:
                st.write("Object distance cannot be zero in this model.")
        elif st.session_state.selected_topic == "Lenses":
            focal = st.slider("Focal length f (cm)", 5, 50, 20)
            object_dist = st.slider("Object distance u (cm)", 5, 100, 40)
            if object_dist != 0:
                image_dist = 1 / (1 / focal - 1 / object_dist) if (1 / focal - 1 / object_dist) != 0 else float('inf')
                magnification = image_dist / object_dist
                st.write(f"Image distance v ≈ **{image_dist:.1f} cm**")
                st.write(f"Magnification m ≈ **{magnification:.2f}**")
                st.write("This hands-on visualization shows how lenses focus light and form images.")
            else:
                st.write("Object distance cannot be zero in this model.")
        else:
            st.write("Use the controls above to explore the topic interactively.")

    st.markdown("---")
    st.write("### Summary of formulas")
    if st.session_state.selected_topic == "Reflection of Light" or st.session_state.selected_topic == "Laws of Reflection":
        st.latex(r"i = r")
    if st.session_state.selected_topic == "Refraction of Light" or st.session_state.selected_topic == "Laws of Refraction":
        st.latex(r"n_1 \sin i = n_2 \sin r")
    if st.session_state.selected_topic == "Formation of Image by a Plane Mirror":
        st.latex(r"v = u")
    if st.session_state.selected_topic == "Spherical Mirrors" or st.session_state.selected_topic == "Magnification and Mirror Formula":
        st.latex(r"\frac{1}{f} = \frac{1}{v} + \frac{1}{u}")
        st.latex(r"m = -\frac{v}{u}")
    if st.session_state.selected_topic == "Lenses":
        st.latex(r"\frac{1}{f} = \frac{1}{v} - \frac{1}{u}")
        st.latex(r"m = \frac{v}{u}")

else:
    st.warning("Select a topic and click the button on the sidebar to load deep information and formulas.")
