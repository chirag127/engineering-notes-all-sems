 Here is the content in Markdown format:

### Location Management: HLR-VLR, Hierarchical, Handoffs

**HLR-VLR**: In GSM networks, location management is done using Home Location Register (HLR) and Visitor Location Register (VLR). HLR stores permanent data of subscribers along with their current location. VLR stores temporary data of subscribers within its geographical area. When a mobile subscriber moves to a new area, the VLR of that area requests data from HLR and updates its records. This helps in keeping track of subscriber location and routing calls to them.

**Hierarchical**: The geographical area is divided into multiple regions with each region having its own VLR. This forms a hierarchy with the top level having HLR. As the subscriber moves far from home area, queries are directed to higher levels in hierarchy and finally to HLR when required. This hierarchical structure reduces the number of queries to HLR and improves efficiency.

**Handoffs**: As the mobile subscriber moves across cells, the call is transferred from one base station to the other without disconnecting the call. This process is known as handoff. Handoffs can be hard, soft or softer depending on whether the channel is changed or not. Handoffs must be performed quickly to avoid call drops. They require accurate measurement of signal strengths from multiple base stations to determine the right time for handoff.

**MNemonics/Tricks**:
- HLR: Home, Permanent
- VLR: Visitor, Temporary
- Hierarchy: Less queries to HLR at higher levels
- Handoff: Call transfer between cells, avoid call drops

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.