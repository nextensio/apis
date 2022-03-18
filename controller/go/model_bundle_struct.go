/*
 * Controller APIs
 *
 * APIs to act on Nextensio Controller
 *
 * API version: 1.0.0
 * Contact: development@nextensio.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type BundleStruct struct {
	Bid string `json:"bid"`
	Connectid string `json:"connectid,omitempty"`
	Cpodrepl int32 `json:"cpodrepl"`
	Name string `json:"name"`
	Services []string `json:"services"`
	Gateway string `json:"gateway,omitempty"`
	Pod string `json:"pod"`
	SharedKey string `json:"sharedKey,omitempty"`
}