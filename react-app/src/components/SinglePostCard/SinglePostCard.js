import React, { useState } from "react";
import {NavLink} from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
// import {Like} from "../images/empty_heart.svg"
import { ImHeart } from "react-icons/im";
import "./SinglePostCard.css";
const SinglePostCard = ({ singlePost }) => {
  const [imageIndex, setImageIndex] = useState(0);
  const number_of_all_comments = 5
  return (
    <div className="single_post_container">
      <div className="single_post_user">
        <img
          src={singlePost.user.profile_photo}
          alt="profile_photo"
          className="profile_photo"
        />
        <p className="user_name">{singlePost.user.username}</p>
      </div>
      <div className="main_post_image">
        <img
          src={singlePost.photos[imageIndex].photo_url}
          alt="display_image"
          className="display_image"
        />
      </div>
      <div className="operation">
        <ImHeart />
        {/* <img src={Like} alt="empty heart"className="empty_heart"/> */}
      </div>
      <div className="likes">
        <p>3 likes</p>
      </div>
      <div className="description">
        <NavLink to="" className="description_user_name"><p>{singlePost.user.username}</p></NavLink>
        <p className="description_content">{singlePost.description}</p>
      </div>
      <div className="view_all_comments">
       <span>view all {number_of_all_comments} comments</span>
      </div>
    </div>
  );
};

export default SinglePostCard;