/*
 * Controller APIs
 *
 * APIs to act on Nextensio Controller
 *
 * API version: 1.0.0
 * Contact: developer@nextensio.com
 * Generated by: Swagger Codegen (https://github.com/swagger-api/swagger-codegen.git)
 */
package swagger

type UserDetails struct {
	Result string `json:"Result"`
	Uid string `json:"uid"`
	Name string `json:"name"`
	Email string `json:"email"`
	Gateway string `json:"gateway"`
	Usertype string `json:"usertype"`
	Pod int32 `json:"pod"`
	Connectid string `json:"connectid,omitempty"`
	Services []string `json:"services"`
}
